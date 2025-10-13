from langgraph.graph import StateGraph, END
from .state import GraphState
from app.features.agentv2.nodes.router import router_node
from app.features.agentv2.nodes.actions import greet_node, send_email_node


def create_workflow():
    workflow = StateGraph(GraphState)

    workflow.add_node("router", router_node)
    workflow.add_node("greet", greet_node)
    workflow.add_node("send_email", send_email_node)

    workflow.set_entry_point("router")

    workflow.add_conditional_edges(
        "router",
        lambda x: x["tool"],
        {
            "greet": "greet",
            "send_email": "send_email",
            "none": END
        }
    )

    workflow.add_edge("greet", END)
    workflow.add_edge("send_email", END)

    return workflow.compile()

app = create_workflow()
