from datetime import datetime
from cognee.shared.data_models import DefaultGraphModel, Relationship, UserProperties, UserLocation
from cognee.modules.cognify.graph.create import create_semantic_graph

async def initialize_graph(root_id: str, graphdatamodel):
    if graphdatamodel:
        graph = graphdatamodel(id= root_id)
        await create_semantic_graph(graph)
    else:
        graph = DefaultGraphModel(
            id=root_id,
            user_properties=UserProperties(
                custom_properties={"age": "30"},
                location=UserLocation(
                    location_id="ny",
                    description="New York",
                    default_relationship=Relationship(type="located_in")
                )
            ),
            default_fields={
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )

        await create_semantic_graph(graph)
