# [KAIRO] Knowledge Graph Visualization Page
# Academic References: SciPy Proceedings 2020 (Pyvis/VisJS),
#   CM4AI CEUR WS 2025 (KG + LLM Reasoning),
#   Karpathy LLM Wiki 2026 (Single-file KB architecture)
import streamlit as st
from core import KBManager, KnowledgeGraph, LLMClient
from pyvis import network as net
from stvis import pv_static
import re

st.set_page_config(page_title="Knowledge Graph - Kairo", page_icon="🧩", layout="wide")
st.title("🧩 Knowledge Graph Visualization")

# Academic reference badge (as proposed in Issue #3)
st.caption(
    "📚 Powered by [Pyvis/VisJS](https://proceedings.scipy.org) (SciPy 2020) "
    & "\u0026 [CM4AI KG+LLM](https://ceur-ws.org/Vol-3773/paper2.pdf) (CEUR WS 2025)"
)

kb = KBManager()
kb_content = kb.read()
edges = KnowledgeGraph.parse_edges(kb_content)

# [ACADEMIC] LLM-based graph interpretation (CM4AI paper §3)
# User can select a node to get LLM-generated natural language interpretation
selected_node = st.session_state.get("graph_selected_node", None)

# Check if LLM is available for interpretation
llm = LLMClient()
llm_ready = bool(llm.api_key)

col1, col2 = st.columns([2, 1])

with col2:
    st.subheader("📋 Edge 목록")
    if edges:
        for i, edge in enumerate(edges):
            with st.container(border=True):
                st.markdown(f"**{edge.get('name', '연결')}**")
                st.caption(f"{edge.get('source', '?')} → {edge.get('target', '?')}")
                st.write(f"유형: {edge.get('type', '일반')}")
    else:
        st.info("Knowledge Graph에 edge가 없습니다.\nKB.md의 Knowledge Graph 섹션에 edge를 추가해주세요.")

    # [ACADEMIC] CM4AI-inspired LLM reasoning panel
    st.divider()
    st.subheader("🧠 LLM 그래프 해석")
    st.caption("CM4AI 논문 기반: Knowledge Graph + LLM Reasoning")
    
    if not llm_ready:
        st.info("⚠️ LLM API 키가 설정되지 않았습니다. \nSettings 페이지에서 API 키를 설정해주세요.")
    elif selected_node:
        # Build prompt based on CM4AI paper: node-centric reasoning
        related_edges = [e for e in edges if e.get('source') == selected_node or e.get('target') == selected_node]
        
        if related_edges:
            prompt = f"""아래 Knowledge Graph에서 '{selected_node}' 노드의 의미와 관계를 한국어로 2~3문장으로 요약해주세요. 마크다운 문법 없이 plain text로.
            
노드 관계:
"""
            for e in related_edges:
                prompt += f"- {e.get('source')} --[{e.get('type')}]--> {e.get('target')}\n"
            
            if st.button("🧠 AI 해석 생성", key="interpret_graph"):
                with st.spinner("LLM이 해석 중..."):
                    interp = llm.chat([{"role": "user", "content": prompt}], kb_content=kb_content, max_tokens=200)
                st.markdown(f"**'{selected_node}' 해석:**")
                st.write(interp)
        else:
            st.info(f"'{selected_node}'와 연결된 edge가 없습니다.")
    else:
        st.info("👈 그래프에서 노드를 클릭하면 LLM이 해석을 제공합니다.")

with col1:
    st.subheader("🌐 그래프 뷰")
    
    if edges:
        # pyvis 그래프 생성
        g = net.Network(height='600px', width='100%', bgcolor='#ffffff', font_color='#333333')
        
        # 노드 추가 (중복 방지)
        added_nodes = set()
        
        for edge in edges:
            source = edge.get('source', '').strip()
            target = edge.get('target', '').strip()
            
            if source and source not in added_nodes:
                g.add_node(source, label=source, title=source, color='#4CAF50')
                added_nodes.add(source)
            
            if target and target not in added_nodes:
                g.add_node(target, label=target, title=target, color='#2196F3')
                added_nodes.add(target)
            
            if source and target:
                edge_type = edge.get('type', '관계')
                g.add_edge(source, target, title=edge_type, label=edge_type)
        
        # 그래프 레이아웃 설정
        g.set_options("""
        {
            "physics": {
                "barnesHut": {
                    "gravitationalConstant": -5000,
                    "centralGravity": 0.3,
                    "springLength": 200,
                    "springConstant": 0.04,
                    "damping": 0.5
                },
                "minVelocity": 0.75,
                "solver": "barnesHut"
            },
            "edges": {
                "arrows": {
                    "to": {"enabled": true, "scaleFactor": 0.5}
                },
                "color": {"inherit": true},
                "smooth": {"enabled": true, "type": "dynamic"}
            },
            "nodes": {
                "font": {"size": 16, "face": "Malgun Gothic"},
                "size": 25,
                "borderWidth": 2
            }
        }
        """)
        
        # [ACADEMIC] Node selection for LLM reasoning (CM4AI pattern)
        all_nodes = sorted(list(added_nodes))
        if all_nodes:
            selected = st.selectbox(
                "🔍 노드 선택 (LLM 해석)",
                ["-- 선택 --"] + all_nodes,
                key="node_selector"
            )
            if selected != "-- 선택 --":
                st.session_state["graph_selected_node"] = selected
                st.rerun()
        
        # Streamlit에 표시
        pv_static(g)
        
        st.caption("💡 노드를 드래그해서 이동할 수 있습니다. 마우스 휠로 확대/축소가 가능합니다.")
    else:
        st.info("🧩 표시할 지식 그래프가 없습니다.\nKB.md의 Knowledge Graph 섹션에 관계(Edge)를 추가해주세요.")

# 하단: KB.md Knowledge Graph 섹션 직접 편집
with st.expander("✏️ KB.md Knowledge Graph 직접 편집"):
    st.markdown("KB.md의 `Knowledge Graph` 섹션을 직접 수정할 수 있습니다.")
    
    # KB.md에서 Knowledge Graph 섹션만 추출
    graph_section = ""
    lines = kb_content.split("\n")
    in_graph = False
    for line in lines:
        if "Knowledge Graph" in line and line.startswith("##"):
            in_graph = True
        if in_graph:
            graph_section += line + "\n"
            if line.startswith("## ") and "Knowledge Graph" not in line:
                in_graph = False
                graph_section = graph_section[:-len(line)-1]
    
    edited_graph = st.text_area("Knowledge Graph 내용", value=graph_section, height=300)
    
    if st.button("💾 그래프 저장하고 새로고침", use_container_width=True):
        # KB.md 전체에서 Knowledge Graph 섹션 교체
        if graph_section:
            new_content = kb_content.replace(graph_section, edited_graph)
            kb.write(new_content)
            st.toast("Knowledge Graph가 저장되었습니다!", icon="✅")
            st.rerun()
