PROTO_DIR = proto
PROTO_FILE = $(PROTO_DIR)/calculator.proto

.PHONY: proto server client

proto:
	python -m grpc_tools.protoc -I$(PROTO_DIR) --python_out=$(PROTO_DIR) --grpc_python_out=$(PROTO_DIR) $(PROTO_FILE)

server:
	python server/server.py

client:
	python client/client.py
