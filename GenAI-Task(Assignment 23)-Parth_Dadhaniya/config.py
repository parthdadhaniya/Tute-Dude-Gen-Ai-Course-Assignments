# config.py - environment setup and tiktoken fix
# Parth Dadhaniya

import os
import sys
import types
import warnings

warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# fix for tiktoken dll lock on windows if needed
try:
    import tiktoken
except Exception:
    dummy = types.ModuleType("tiktoken")
    dummy.Encoding = type("Encoding", (), {
        "encode": lambda s, text, *a, **k: text.split(),
        "decode": lambda s, tokens, *a, **k: " ".join(tokens)
    })
    dummy.get_encoding = lambda name: dummy.Encoding()
    dummy.encoding_for_model = lambda name: dummy.Encoding()
    sys.modules["tiktoken"] = dummy
