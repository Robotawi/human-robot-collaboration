import os
import copy
import numpy as np
import environment.collisionmodel as cm
from panda3d.core import NodePath
from utiltools import robotmath as rm


def buildCabinet(base, cabpos = np.array([773.5, -55.17, 1035]), cabrotangle = 0, isrendercoord = False):
    __this_dir, _ = os.path.split(__file__)
    cabinet = NodePath("cabinet")
    #build the cabinet
    #the middle board, 3 pieces
    middleboardpath = os.path.join(__this_dir, "objects", "middleboard.stl")
    middleboard0 = cm.CollisionModel(middleboardpath, radius=3, betransparency=True)

    middleboard0.setColor(1,0,0,1)
    temprotmiddleboard = rm.rodrigues([0,0,1],90)
    rotmiddleboardmat4 = middleboard0.getMat()
    rotmiddleboardnp4 = base.pg.mat4ToNp(rotmiddleboardmat4)
    rotmiddleboardnp4[:3,:3] = np.dot(temprotmiddleboard, rotmiddleboardnp4[:3,:3])
    rotmiddleboardmat4 = base.pg.np4ToMat4(rotmiddleboardnp4)
    middleboard0.setMat(rotmiddleboardmat4)

    # temprotsmallboard = np.dot()
    middleboard1 = copy.deepcopy(middleboard0)
    middleboard1.setPos(0,0,288.5)
    middleboard2 = copy.deepcopy(middleboard0)
    temprotmiddleboard = rm.rodrigues([1,0,0],180)
    rotmiddleboardnp4[:3, :3] = np.dot(temprotmiddleboard, rotmiddleboardnp4[:3, :3])
    rotmiddleboardnp4[:3, 3] = np.array([0, 0, 587])
    middleboard2.sethomomat(rotmiddleboardnp4)

    # middleboard2.setPos(0,0,577)


    middleboard0.setColor(.4,.4,.4,.7) #this 0 doesn't need to setpos
    middleboard0.reparentTo(cabinet)
    middleboard1.setColor(.4,.4,.4,.7)
    middleboard1.reparentTo(cabinet)
    middleboard2.setColor(.4,.4,.4,.7)
    middleboard2.reparentTo(cabinet)

    largeboardpath = os.path.join(__this_dir, "objects", "largeboard.stl")

    largeboard0 = cm.CollisionModel(largeboardpath, radius=3, betransparency=True)
    largeboard1 = copy.deepcopy(largeboard0)
    largecompundrot0 = np.dot(rm.rodrigues([0, 1, 0], -90),rm.rodrigues([1, 0, 0], 90))
    largecompundrot1 = np.dot(rm.rodrigues([-1, 0, 0], 180), largecompundrot0)
    largeboard0.sethomomat(rm.homobuild(np.array([0,195,293.5]), largecompundrot0))
    largeboard1.sethomomat(rm.homobuild(np.array([0,-195,293.5]), largecompundrot1))

    largeboard0.setColor(.4,.4,.4,.7)
    largeboard0.reparentTo(cabinet)
    largeboard1.setColor(.4,.4,.4,.7)
    largeboard1.reparentTo(cabinet)

    # the small board, 2 pieces
    smallboardpath = os.path.join(__this_dir, "objects", "smallboard.stl")
    smallboard0 = cm.CollisionModel(smallboardpath, radius=3, betransparency=True)
    smallboard1 = copy.deepcopy(smallboard0)

    smallcompundrot = np.dot(rm.rodrigues([0, 1, 0], 90),rm.rodrigues([0, 0, 1], -90))

    smallboard0.sethomomat(rm.homobuild(np.array([-142.5,0,149.25]), smallcompundrot))
    smallboard1.sethomomat(rm.homobuild(np.array([-142.5,0,587-149.25]), smallcompundrot))
    smallboard0.setColor(.4,.4,.4,.7)
    smallboard0.reparentTo(cabinet)
    smallboard1.setColor(.4,.4,.4,.7)
    smallboard1.reparentTo(cabinet)

    if isrendercoord == True:
        middleboard0.showLocalFrame()
        middleboard1.showLocalFrame()
        middleboard2.showLocalFrame()
        largeboard0.showLocalFrame()
        largeboard1.showLocalFrame()
        smallboard0.showLocalFrame()
        smallboard1.showLocalFrame()

    #rotate the cabinet
    cabinetassemblypos = cabpos # on the edge is 773, a bit outside is 814
    cabinetassemblyrot = rm.rodrigues([0, 0, 1], cabrotangle)
    cabinet.setMat(base.pg.np4ToMat4(rm.homobuild(cabinetassemblypos,cabinetassemblyrot)))

    return cabinet
