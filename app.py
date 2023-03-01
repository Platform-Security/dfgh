import docker
client=docker.from_env()
image, logs =client.images.build(path='https://github.com/professorJordan/platform_security.git',tag='my-docker')
for line in logs:
    print(line)

for line in client.images.push('my-docker-image', stream=True, auth_config={
    'username': 'platformsecurityusa',
    'password': 'paper.success'
}):
    print(line)
