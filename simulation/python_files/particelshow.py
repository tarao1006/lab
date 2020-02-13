showRigidCOM = 0
withoutPBC = 0
getPos = lambda n: $Particles[n].R  # noqa
getCOM = lambda n: $Particles[n].R  # noqa
getQua = lambda n: $Particles[n].q  # noqa

type = $constitutive_eq.type
if type == "Navier_Stokes":
    dx = $constitutive_eq.Navier_Stokes.DX
elif type == "Shear_Navier_Stokes":
    dx = $constitutive_eq.Shear_Navier_Stokes.DX

LX = dx * (2 ** $mesh.NPX)
LY = dx * (2 ** $mesh.NPY)
LZ = dx * (2 ** $mesh.NPZ)

shear_rate_v = 0.5 * LY * $constitutive_eq.Shear_Navier_Stokes.External_field.DC.Shear_rate
Ns = getArray($object_type.spherical_particle.Particle_spec[])
size_Ns = len(Ns)
RAD = ($A * dx) * 1.0
cells = [[0, 0, 0], [0, LY, 0], [LX, LY, 0], [LX, 0, 0], [0, 0, 0], [0, 0, LZ], [LX, 0, LZ], [LX, LY, LZ], [0, LY, LZ], [0, 0, LZ]]
polyline(cells, 1)
line([0, LY, 0], [0, LY, LZ], 1)
line([LX, 0, 0], [LX, 0, LZ], 1)
line([LX, LY, 0], [LX, LY, LZ], 1)
spat = [
    [1.0, 0.0, 0.0, 1.0, RAD],
    [0.0, 1.0, 0.0, 1.0, RAD],
    [0.0, 0.0, 1.0, 1.0, RAD],
    [1.0, 1.0, 0.0, 1.0, RAD],
    [0.0, 1.0, 1.0, 1.0, RAD],
    [1.0, 0.0, 1.0, 1.0, RAD],
    [1.0, 1.0, 1.0, 1.0, RAD]
]
n_offset = 0


def quaternionToRotationArray(q):
    w = q[0]
    x = q[1]
    y = q[2]
    z = q[3]

    xx = x * x
    yy = y * y
    zz = z * z

    xy = x * y
    yz = y * z
    zx = z * x

    wx = w * x
    wy = w * y
    wz = w * z

    return [
        [1 - 2 * (yy + zz), 2 * (xy + wz), 2 * (zx - wy)],
        [2 * (xy - wz), 1 - 2 * (xx + zz), 2 * (yz + wx)],
        [2 * (zx + wy), 2 * (yz - wx), 1 - 2 * (xx - yy)]
    ]


for i in range(size_Ns):
    for n in range(Ns[i][0]):
        r = getPos(n_offset + n)
        q = getQua(n_offset + n)
        rotation_matrix = quaternionToRotationArray(q)
        uv = [
            r[0] + rotation_matrix[1][0],
            r[1] + rotation_matrix[1][1],
            r[2] + rotation_matrix[1][2]
        ]
        arrow(r, uv, [255, 255, 255, 1, 1, 1, 10])
        sphere(r, spat[i % len(spat)])
    n_offset += Ns[i][0]
