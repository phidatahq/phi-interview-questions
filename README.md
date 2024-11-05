## Phidata Interview Questions

## Setup

1. Clone the repo

```sh
git clone https://github.com/phidatahq/phi-interview-questions.git
```

2. Install requirements and activate the virtual env:

> Install uv if needed: `curl -LsSf https://astral.sh/uv/install.sh | sh`

```sh
./scripts/install.sh
source .venv/bin/activate
```

3. Run Agent team

```sh
python agent_team.py
```

4. Start local docker containers

```sh
phi start dev_resources.py
```

5. Open swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs) to test the API.

6. Stop local docker containers

```sh
phi stop dev_resources.py
```
