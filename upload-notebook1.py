import azureml.core
from azureml.core.model import Model
from azureml.core import Workspace
import sys

workspace=sys.argv[0]
subscription_id=sys.argv[1]
resource_group=sys.argv[2]

ws = Workspace.get(
     name=workspace, 
     subscription_id=subscription_id,
     resource_group=resource_group
     )

file_model = Model.register(model_path = "./model.mlmodel", # this points to a local file
                       model_name = "nyc-taxi-automl-predictor", # name the model is registered as
                       tags = {'area': "auto", 'type': "regression"}, 
                       description = "NYC Taxi Fare Predictor", 
                       workspace = ws)

ml_client.models.create_or_update(file_model)

