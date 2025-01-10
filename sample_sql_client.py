from vantage6.client import UserClient as Client

# Note: we assume here the config.py you just created is in the current directory.
# If it is not, then you need to make sure it can be found on your PYTHONPATH
import config

# Initialize the client object, and run the authentication
client = Client(config.server_url, config.server_port, config.server_api,
                log_level='debug')
client.authenticate(config.username, config.password)

# Optional: setup the encryption, if you have an organization_key
client.setup_encryption(config.organization_key)

input_ = {
    'method': 'central_average',
    'kwargs': {"column_name":"VALUE"}
}

average_task = client.task.create(
   collaboration=2,
   organizations=[7],
   name="poc-cli-lifelines-central-avg-dec-3",
   image="harbor2.vantage6.ai/demo/average",
   description='',
   input_=input_,
   databases=[
      {'label': 'lifelines', 'query': 'select VALUE FROM CREATININE'}
   ]
)

task_id = average_task['id']
print('Waiting for results...')
result = client.wait_for_results(task_id)
print('Results received!')
print(result)