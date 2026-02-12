import numpy as np

def compute_homography(src_pts, dst_pts):
    n = src_pts.shape[0]
    A = []

    for i in range(n):
        x, y = src_pts[i][0], src_pts[i][1]
        xp, yp = dst_pts[i][0], dst_pts[i][1]

        A.append([-x, -y, -1, 0, 0, 0, x*xp, y*xp, xp])
        A.append([0, 0, 0, -x, -y, -1, x*yp, y*yp, yp])

    A = np.array(A)

    U, S, Vt = np.linalg.svd(A)
    H = Vt[-1].reshape(3, 3)
    H = H / H[2, 2]

    return H

src_points = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
])

dst_points = np.array([
    [0, 0],
    [2, 0],
    [2, 2],
    [0, 2]
])

H = compute_homography(src_points, dst_points)
print(H)
