rm pycram_bullet.pb.cpp
rm pycram_bullet.pb.h
rm pycram_bullet.grpc.pb.cpp
rm pycram_bullet.grpc.pb.h

protoc --proto_path=. --cpp_out=. pycram_bullet.proto
protoc --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` --grpc_out=. pycram_bullet.proto
mv pycram_bullet.grpc.pb.cc pycram_bullet.grpc.pb.cpp
mv pycram_bullet.pb.cc pycram_bullet.pb.cpp

rm pycram_bullet_pb2.py
rm pycram_bullet_pb2_grpc.py

protoc --proto_path=. --python_out=. pycram_bullet.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pycram_bullet.proto
