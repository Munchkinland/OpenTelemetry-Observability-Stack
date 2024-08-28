from flask import Flask
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import set_tracer_provider

app = Flask(__name__)

# Configura OpenTelemetry
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configura el exportador OTLP
otlp_exporter = OTLPSpanExporter(endpoint="http://collector:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

@app.route('/')
def home():
    with tracer.start_as_current_span("home_span"):
        return "Hello, OpenTelemetry!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
