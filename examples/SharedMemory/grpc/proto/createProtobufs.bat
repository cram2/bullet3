del pycram_bullet.pb.cpp
del pycram_bullet.pb.h
del pycram_bullet.grpc.pb.cpp
del pycram_bullet.grpc.pb.h

..\..\..\ThirdPartyLibs\grpc\lib\win32\protoc --proto_path=. --cpp_out=. pycram_bullet.proto
..\..\..\ThirdPartyLibs\grpc\lib\win32\protoc.exe --plugin=protoc-gen-grpc="..\..\..\ThirdPartyLibs\grpc\lib\win32\grpc_cpp_plugin.exe" --grpc_out=. pycram_bullet.proto

rename pycram_bullet.grpc.pb.cc pycram_bullet.grpc.pb.cpp
rename pycram_bullet.pb.cc pycram_bullet.pb.cpp

del pycram_bullet_pb2.py
del pycram_bullet_pb2_grpc.py

..\..\..\ThirdPartyLibs\grpc\lib\win32\protoc --proto_path=. --python_out=. pycram_bullet.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pycram_bullet.proto
