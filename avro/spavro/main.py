import time
import io

from spavro.schema import parse
from spavro.io import FastDatumWriter
from spavro.fast_binary import FastBinaryEncoder


def test_spavro(size):
    schema = parse("""{
        "type": "record",
        "name": "test_schema",
        "fields": [
            {
                "name": "time",
                "type": "long"
            },
            {
                "name": "customer",
                "type": "string"
            }
        ]
    }""")
    out = io.BytesIO()
    writer = FastDatumWriter(schema)
    encoder = FastBinaryEncoder(out)
    data = [
        {
			"time":     1717104831727 + i,
			"customer": f"customer{i}",
        } for i in range(size)
    ]

    start = time.time()
    for datum in data:
        out.seek(0)
        out.truncate(0)
        writer.write(datum, encoder)
        # print(out.getvalue())
    print(time.time() - start)
