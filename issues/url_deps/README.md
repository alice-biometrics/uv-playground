## Issue https://github.com/astral-sh/uv/issues/1808

This code try to reproduce an `uv` limitation.

To reproduce this, just run:

```console
pip install "uv==0.1.16"
uv pip install -r requirements.txt
```

Solved in https://github.com/astral-sh/uv/pull/2684 

```console
pip install "uv==0.1.28"
uv pip install -r requirements.txt
```

:party: