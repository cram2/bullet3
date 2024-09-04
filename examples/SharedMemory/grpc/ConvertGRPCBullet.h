
#ifndef BT_CONVERT_GRPC_BULLET_H
#define BT_CONVERT_GRPC_BULLET_H

#include "../PhysicsClientC_API.h"

namespace pycram_bullet_grpc
{
class PyBulletCommand;
class PyBulletStatus;
};  // namespace pycram_bullet_grpc

struct SharedMemoryCommand* convertGRPCToBulletCommand(const pycram_bullet_grpc::PyBulletCommand& grpcCommand, struct SharedMemoryCommand& cmd);

pycram_bullet_grpc::PyBulletCommand* convertBulletToGRPCCommand(const struct SharedMemoryCommand& clientCmd, pycram_bullet_grpc::PyBulletCommand& grpcCommand);

bool convertGRPCToStatus(const pycram_bullet_grpc::PyBulletStatus& grpcReply, struct SharedMemoryStatus& serverStatus, char* bufferServerToClient, int bufferSizeInBytes);

bool convertStatusToGRPC(const struct SharedMemoryStatus& serverStatus, char* bufferServerToClient, int bufferSizeInBytes, pycram_bullet_grpc::PyBulletStatus& grpcReply);

#endif  //BT_CONVERT_GRPC_BULLET_H