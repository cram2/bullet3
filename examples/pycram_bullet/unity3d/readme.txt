Quick prototype to connect Unity 3D to pycram_bullet

Generate C# Native Methods using the Microsoft PInvoke Signature Toolkit:

sigimp.exe  /lang:cs e:\develop\bullet3\examples\SharedMemory\PhysicsClientC_API.h

Add some #define B3_SHARED_API __declspec(dllexport) to the exported methods,
replace [3], [4], [16] by [] to get sigimp.exe working.

This generates autogen/NativeMethods.cs

Then put pycram_bullet.dll in the right location, so Unity finds it.

NewBehaviourScript.cs is a 1 evening prototype that works within Unity 3D:
Create a connection to pycram_bullet, reset the world, load a urdf at startup.
Step the simulation each Update.

Now the real work can start, converting Unity objects to pycram_bullet,
pycram_bullet robots to Unity, synchronizing the transforms each Update.

void Start () {
	IntPtr pycram_bullet = b3ConnectSharedMemory(12347);
	IntPtr cmd = b3InitResetSimulationCommand(pycram_bullet);
	IntPtr status = b3SubmitClientCommandAndWaitStatus(pycram_bullet, cmd);
	cmd = b3LoadUrdfCommandInit(pycram_bullet, "plane.urdf");
	status = b3SubmitClientCommandAndWaitStatus(pycram_bullet, cmd);
}

void Update () 
{
	IntPtr cmd = b3InitStepSimulationCommand(pycram_bullet);
	IntPtr status = b3SubmitClientCommandAndWaitStatus(pycram_bullet, cmd);
}
