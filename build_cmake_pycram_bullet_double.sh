#!/bin/sh

if [ -e CMakeCache.txt ]; then
  rm CMakeCache.txt
fi
mkdir -p build_cmake
cd build_cmake
cmake -DBUILD_PYBULLET=ON -DBUILD_PYBULLET_NUMPY=ON -DUSE_DOUBLE_PRECISION=ON -DBT_USE_EGL=ON -DCMAKE_BUILD_TYPE=Release .. || exit 1
make -j $(command nproc 2>/dev/null || echo 12) || exit 1
cd examples
cd pycram_bullet
if [ -e pycram_bullet.dylib ]; then
  ln -f -s pycram_bullet.dylib pycram_bullet.so
fi
if [ -e pycram_bullet_envs ]; then
  rm pycram_bullet_envs
fi
if [ -e pycram_bullet_data ]; then
  rm pycram_bullet_data
fi
if [ -e pycram_bullet_utils ]; then
  rm pycram_bullet_utils
fi
ln -s ../../../examples/pycram_bullet/gym/pycram_bullet_envs .
ln -s ../../../examples/pycram_bullet/gym/pycram_bullet_data .
ln -s ../../../examples/pycram_bullet/gym/pycram_bullet_utils .
echo "Completed build of Bullet."
