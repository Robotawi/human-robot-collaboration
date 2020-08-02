import os
import time
import numpy as np
import simenvironment as simenv
import environment.collisionmodel as cm
import environment.bulletcdhelper as bch
import dualarmsharedgrasp as sharedgrasp
import utiltools.robotmath as rm
import pandaplotutils.pandactrl as pandactrl
import robotsim.ur3dual.ur3dual as robot
import robotsim.ur3dual.ur3dualmesh as robotmesh
import robotsim.nextage.nxt as human
import robotsim.nextage.nxtmesh as humanmesh
import robotsim.nextage.nxtik as humanik
import manipulation.grip.robotiq85.robotiq85 as rtq85
import manipulation.grip.humanhand.hhdw as hhdw
import copy
from cabinetbuilder import buildCabinet
from cabinetboardsgrasps import boardGrasps

if __name__ == '__main__':
    base = pandactrl.World(camp=[2700, 2300, 2700], lookatp=[800, 0, 1000])

    env = simenv.Env()
    env.reparentTo(base.render)

    #robot hand and arm
    hndfa = rtq85.Robotiq85Factory()
    rgthnd = hndfa.genHand()
    lfthnd = hndfa.genHand()
    rbt = robot.Ur3DualRobot(rgthnd=rgthnd, lfthnd=lfthnd)
    rbtmg = robotmesh.Ur3DualMesh()

    #human hand and arm
    hhdfa = hhdw.HHdwFactory()
    rgthmhnd = hhdfa.genHand(ftsensoroffset=0, armname="rgt")
    lfthmhnd = hhdfa.genHand(ftsensoroffset=0, armname="lft")
    hmn = human.NxtRobot(rgthnd=rgthmhnd, lfthnd=lfthmhnd, position=[1100, 0, 200], rotmat=rm.rodrigues([0,0,1], 180))
    hmnmg = humanmesh.NxtMesh()

    #build the cabinet
    cabinet = buildCabinet(base, isrendercoord=True)
    cabinet.reparentTo(base.render)
    cabinetpose = cabinet.getMat()
    cabinetposenp4 = base.pg.mat4ToNp(cabinetpose)

    __this_dir, _ = os.path.split(__file__)
    largeboardpath = os.path.join(__this_dir, "objects", "largeboard.stl")
    middleboardpath = os.path.join(__this_dir, "objects", "middleboard.stl")
    smallboardpath = os.path.join(__this_dir, "objects", "smallboard.stl")

    # the boards
    largeboard0 = cm.CollisionModel(largeboardpath, radius=3, betransparency=True)
    middleboard0 = cm.CollisionModel(middleboardpath, radius=3, betransparency=True)
    smallboard0 = cm.CollisionModel(smallboardpath, radius=3, betransparency=True)

    # the obstacle boards
    largeboardobstacle0 = copy.deepcopy(largeboard0)
    largecompundrot = np.dot(rm.rodrigues([0, 1, 0], -90), rm.rodrigues([1, 0, 0], 90))
    largeboardobstacle0.sethomomat(rm.homobuild(np.array([0, 195, 293.5]) + cabinetposenp4[:3, 3], largecompundrot))
    largeboardobstacle0.setColor(0, 0, 0, 1)
    # largeboardobstacle0.reparentTo(base.render)

    smallboardobstacle0 = copy.deepcopy(smallboard0)
    smallboardobstacle1 = copy.deepcopy(smallboard0)
    smallcompundrot = np.dot(rm.rodrigues([0, 1, 0], 90), rm.rodrigues([0, 0, 1], -90))

    smallboardobstacle0.sethomomat(rm.homobuild(np.array([-142.5, 0, 149.25]) + cabinetposenp4[:3, 3], smallcompundrot))
    smallboardobstacle1.sethomomat(
        rm.homobuild(np.array([-142.5, 0, 587 - 149.25]) + cabinetposenp4[:3, 3], smallcompundrot))
    # smallboardobstacle0.reparentTo(base.render)
    # smallboardobstacle1.reparentTo(base.render)
    smallboardobstacle0.setColor(0, 0, 0, 1)
    smallboardobstacle1.setColor(0, 0, 0, 1)

    middleboardobstacle0 = copy.deepcopy(middleboard0)
    temprotmiddleboard = rm.rodrigues([0, 0, 1], 90)
    rotmiddleboardmat4 = middleboard0.getMat()
    rotmiddleboardnp4 = base.pg.mat4ToNp(rotmiddleboardmat4)
    rotmiddleboardnp4[:3, :3] = np.dot(temprotmiddleboard, rotmiddleboardnp4[:3, :3])
    rotmiddleboardnp4[:3, 3] = np.array([0, 0, 288.5]) + cabinetposenp4[:3, 3]
    rotmiddleboardmat4 = base.pg.np4ToMat4(rotmiddleboardnp4)
    middleboardobstacle0.setMat(rotmiddleboardmat4)
    middleboardobstacle0.setColor(0, 0, 0, 1)
    # middleboardobstacle0.reparentTo(base.render)

    # what were the obstacles in the motion planning?
    # add here
    # the obstacle boards, large, 2 small, 1 middle
    largeboardobstacle0_ = copy.deepcopy(largeboard0)
    smallboardobstacle0_ = copy.deepcopy(smallboard0)
    smallboardobstacle1_ = copy.deepcopy(smallboard0)
    middleboardobstacle0_ = copy.deepcopy(middleboard0)
    # large
    boardbigobstaclemat4 = np.array([[-5.17437784e-02, -9.95593322e-01, -7.82082644e-02,
                                      7.76528438e+02 - 20],
                                     [3.34583085e-02, 7.65409534e-02, -9.96504898e-01,
                                      1.12262779e+02],
                                     [9.98099753e-01, -5.41796370e-02, 2.93503453e-02,
                                      1.33495368e+03],
                                     [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                                      1.00000000e+00]])
    largeboardobstacle0_.setMat(base.pg.np4ToMat4(boardbigobstaclemat4))
    # largeboardobstacle0_.setColor(0, 0, 0, 1)
    # largeboardobstacle0_.reparentTo(base.render)
    # small
    board3mmobstaclemat4 = np.array([[-4.06201696e-02, 7.16858009e-02, 9.96599799e-01, 6.46767555e+02 - 20],
                                     [-9.99056654e-01, -1.82425841e-02, -3.94081142e-02, -9.09652698e+01],
                                     [1.53555473e-02, -9.97260422e-01, 7.23591817e-02, 1.18896190e+03],
                                     [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
    smallboardobstacle0_.setMat(base.pg.np4ToMat4(board3mmobstaclemat4))
    # smallboardobstacle0_.reparentTo(base.render)
    board3mm2obstaclemat4 = np.array([[-4.06201696e-02, 7.16858009e-02, 9.96599799e-01, 6.46767555e+02 - 20 - 20],
                                      [-9.99056654e-01, -1.82425841e-02, -3.94081142e-02, -9.09652698e+01],
                                      [1.53555473e-02, -9.97260422e-01, 7.23591817e-02, 1.18896190e+03 + 288 + 5],
                                      [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
    smallboardobstacle1_.setMat(base.pg.np4ToMat4(board3mm2obstaclemat4))
    # smallboardobstacle1_.reparentTo(base.render)
    # middle
    board10mmcenterobstaclemat4 = np.array([[4.33228738e-02, -9.95782460e-01, -8.08729688e-02,
                                             7.90728365e+02 - 20],
                                            [9.98924573e-01, 4.18364924e-02, 1.99849488e-02,
                                             -7.50286830e+01],
                                            [-1.65172165e-02, -8.16517971e-02, 9.96524034e-01,
                                             1.33800992e+03],
                                            [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                                             1.00000000e+00]])
    middleboardobstacle0_.setMat(base.pg.np4ToMat4(board10mmcenterobstaclemat4))
    # middleboardobstacle0_.reparentTo(base.render)

    # base.run()

    # for the handover goal calculation middleboard0
    middleboard0 = cm.CollisionModel(middleboardpath, radius=3, betransparency=True)
    # middleboard0.setColor(1,1,0,0.5)
    temprotmiddleboard = rm.rodrigues([0,0,1],90)
    rotmiddleboardmat4 = middleboard0.getMat()
    rotmiddleboardnp4 = base.pg.mat4ToNp(rotmiddleboardmat4)
    rotmiddleboardnp4[:3,:3] = np.dot(temprotmiddleboard, rotmiddleboardnp4[:3,:3])
    rotmiddleboardmat4 = base.pg.np4ToMat4(rotmiddleboardnp4)
    middleboard0.setMat(rotmiddleboardmat4)
    middleboard0.setColor(1,0,0,0.5)
    # middleboard0.reparentTo(base.render)
    # base.run()

    # calculate the assmebly pose in the world frame
    middleboardassembly = copy.deepcopy(middleboard0)

    middleboardassembly.setColor(1, 1, 0, 0.5)
    middleboardassembly.showLocalFrame()

    # middleboardassembly.sethomomat(rm.homobuild(np.array([0, 0, 0]) + cabinetposenp4[:3, 3], largecompundrot1))
    middleboardassembly.setPos(cabinetposenp4[0, 3], cabinetposenp4[1, 3], cabinetposenp4[2, 3]+288.5)
    middleboardassembly.reparentTo(base.render)
    middleboardassembly.showLocalFrame()
    middleboardassemblymat4 = middleboardassembly.getMat()
    middleboardassemblymat4 = base.pg.mat4ToNp(middleboardassemblymat4)

    largeboardobstacle0.setColor(1, 1, 1, 1)

    bcdchecker = bch.MCMchecker(toggledebug=False)
    
    # sample the candidate handove poses wrt the final assembly part and check collision detection with already assembled parts
    testgoalmatspace = []
    for rotangle in range(20, 30, 10):
        for trans_y in range(0, 200, 100):
            for trans_x in range(0, 500, 100):
                for trans_z in range(100, 300, 50):
                    testboard = copy.deepcopy(middleboardassembly)
                    testmat4 = np.eye(4)
                    testmat4[:3, :3] = middleboardassemblymat4[:3, :3]
                    testmat4[:3, :3] = np.dot(middleboardassemblymat4[:3, :3], rm.rodrigues(middleboardassemblymat4[:3, 2], -1*rotangle))  # fix the rotation here!
                    testmat4[:3, 3] = middleboardassemblymat4[:3, 3] + trans_z * middleboardassemblymat4[:3,2] + trans_y * middleboardassemblymat4[ :3, 0] + trans_x * middleboardassemblymat4[ :3, 1]
                    testboard.setMat(base.pg.np4ToMat4(testmat4))
                    isbrdcollided = bcdchecker.isMeshMeshCollided(largeboardobstacle0_, testboard)

                    if not isbrdcollided:
                        testgoalmatspace.append(testmat4)
                        testboard.setColor(1, 1, 1, .5)
                        # testboard.reparentTo(base.render)
                    else:
                        print("collided board detected!")
                        # testgoalmatspace.append(testmat4)
                        # testboard.setColor(0.9, 0.5, 0.5, .5)
                        # testboard.reparentTo(base.render)

    print("Length of test mat space is ", len(testgoalmatspace))


    #load the board predefined grasps
    premiddle = boardGrasps(board='middle')

    # check the shared grasps between the above goal and start pose
    # the start and the original goal poses
    brdmat4upstart = np.array([[7.53733449e-01, -6.56633500e-01, -2.68019739e-02,
                                4.72763116e+02],
                               [6.56864713e-01, 7.54008416e-01, -2.34611181e-04,
                                1.52724830e+01],
                               [2.03629596e-02, -1.74284332e-02, 9.99640728e-01,
                                1.05198582e+03],
                               [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                                1.00000000e+00]])
    brdposstart_set = [340, -100, 1250]
    brdmat4upstart[:3, 3] = brdposstart_set

    temprotstart = rm.rodrigues(brdmat4upstart[:3, 2], 40)
    brdmat4upstart[:3, :3] = np.dot(temprotstart, brdmat4upstart[:3, :3])
    brdmat4goal = np.array([[5.84475086e-01, -8.09356797e-01, -5.77101876e-02,
                          4.45694324e+02],
                         [8.11410877e-01, 5.83093079e-01, 4.01851111e-02,
                          -2.92055328e+01],
                         [1.12631877e-03, -7.03138670e-02, 9.97524273e-01,
                          1.41582538e+03],
                         [0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
                          1.00000000e+00]])
    temprot = rm.rodrigues(brdmat4goal[:3,2],15)
    brdmat4goal[:3,:3] = np.dot(temprot,brdmat4goal[:3,:3])
    brdposgoal_set = [0, 100, -80]
    brdmat4goal[:3, 3] = brdmat4goal[:3, 3] - brdposgoal_set


    #visualize start
    middleboardstart = copy.deepcopy(middleboard0)
    middleboardstart.setMat(base.pg.np4ToMat4(brdmat4upstart))
    middleboardstart.setColor(0, 0, 1, 0.5)
    middleboardstart.showLocalFrame()
    middleboardstart.reparentTo(base.render)

    #visualiza goal
    middleboardgoal = copy.deepcopy(middleboard0)
    middleboardgoal.setMat(base.pg.np4ToMat4(brdmat4goal))
    middleboardgoal.setColor(0, 0, 0, 1)
    middleboardgoal.showLocalFrame()
    middleboardgoal.reparentTo(base.render)


    ### the human part ###
    # brdmat4goal = selectedbrdgoalmat4
    import matplotlib.pyplot as plt
    cmap = plt.get_cmap('rainbow')
    availablecomfortabletestgoallist = [] #if ok for both hands
    graspsforavailablecomfortabletestgoallist = []

    #for each candidate goal handover pose in the testgoal space check the availablility for comfortable human grasps, and save the poses that are comfortable for the next step
    for testgoalid, testgoalmat in enumerate(testgoalmatspace):
        tic = time.time()
        iclistrgt = []
        availablehmngraspsrgt = []
        iclistlft = []
        availablehmngraspslft = []

        for idgc, gc in enumerate(premiddle):
            eerot = np.dot(testgoalmat[:3, :3], gc[2][:3, :3])
            eepos = np.dot(testgoalmat[:3, :3], gc[1]) + testgoalmat[:3, 3]
            boardcom = testgoalmat[:3, 3]

            # the board center and the cabinet pose
            if np.linalg.norm(boardcom - eepos) < 200:
                rgtjnts = hmn.numik(eepos, eerot, armname='rgt')
                if rgtjnts is not None :
                    hmn.movearmfk(rgtjnts, armname='rgt')
                    ic = humanik.manipulability_inversecondition(hmn, armname='rgt') * 700
                    # print("for the right human hand grasp ", idgc,", its quality ic is ", ic) #uncomment for debugging
                    if ic >= 0.4:
                        # save the available grasp
                        availablehmngraspsrgt.append(gc)
                        # save the quality of the available human grasps
                        iclistrgt.append(ic)  # rank
                        rgb = cmap(ic)
                        # hmnmnp = hmnmg.gensnp(hmn, drawhand=True, rgbargthnd=np.array([rgb[0],rgb[1],rgb[2],.5]),rgbalftarm=np.array([255,255,255,0]),rgbalfthnd=np.array([255,255,255,0]))
                        # hmnmnp.reparentTo(base.render)

            #if the left arm is to be considered
            if np.linalg.norm(boardcom - eepos) < 200:
                lftjnts = hmn.numik(eepos, eerot, armname='lft')
                if lftjnts is not None:
                    hmn.movearmfk(lftjnts, armname='lft')
                    ic = humanik.manipulability_inversecondition(hmn, armname='lft') * 700
                    # print("for the left human hand grasp ", idgc,", its quality ic is ", ic) #uncomment for debugging
                    if ic >= 0.4:
                        # save the available grasp
                        availablehmngraspslft.append(gc)
                        # save the quality of the available human grasps
                        iclistlft.append(ic) # rank

                        rgb = cmap(ic)
                        # hmnmnp = hmnmg.gensnp(hmn, drawhand=True, rgbalfthnd=np.array([rgb[0],rgb[1],rgb[2],.5]),rgbargtarm=np.array([255,255,255,0]),rgbargthnd=np.array([255,255,255,0]))
                        # hmnmnp.reparentTo(base.render)


        # print("available grasps are ",len(availablehmngraspsrgt)," for rgt arm, and ", len(availablehmngraspslft), " for the lft arm.") #uncomment for debugging
        if len(availablehmngraspsrgt) > 0 and len(availablehmngraspslft) > 0:
            print("Test goal board pose ", testgoalid, " is available for both human hands", "time is ", time.time()-tic)
            iclistindecesrgt = [iclistrgt.index(x) for x in sorted(iclistrgt, reverse=True)]
            # print("length of available human grasps is ", len(availablehmngraspsrgt))
            # print(iclist)
            bestindexrgt = iclistindecesrgt[0]
            # nextbestindexrgt = iclistindecesrgt.index(1)
            # nextnextbestindexrgt = iclistindecesrgt.index(2)
            # print("index of zero (best) is ", bestindexrgt)
            # print("best grasp is, ", availablehmngraspsrgt[bestindexrgt])
            # print("best grasp quality is ", iclistrgt[bestindexrgt])
            besthmngrasprgt = availablehmngraspsrgt[bestindexrgt]

            eerot = np.dot(testgoalmat[:3, :3], besthmngrasprgt[2][:3, :3])
            eepos = np.dot(testgoalmat[:3, :3], besthmngrasprgt[1]) + testgoalmat[:3, 3]

            rgtjnts = hmn.numik(eepos, eerot, armname='rgt')

            # for the lft arm
            iclistindeceslft = [iclistlft.index(x) for x in sorted(iclistlft, reverse=True)]
            # print("length of available human grasps is ", len(availablehmngraspslft))
            # print(iclist)
            # there's a bug here, the index ought to be what?
            bestindexlft = iclistindeceslft[0]
            # nextbestindexlft = iclistindeceslft.index(1)
            # nextnextbestindexlft = iclistindeceslft.index(2)
            # bestindexlft = iclistindeceslft[0]
            # nextbestindexlft = iclistindeceslft[1]
            # nextnextbestindexlft = iclistindeceslft[2]
            # print("index of zero (best) is ", bestindexlft)
            besthmngrasplft = availablehmngraspslft[bestindexlft]

            eerot = np.dot(testgoalmat[:3, :3], besthmngrasplft[2][:3, :3])
            eepos = np.dot(testgoalmat[:3, :3], besthmngrasplft[1]) + testgoalmat[:3, 3]
            #testgoalmat, bro!!!
            lftjnts = hmn.numik(eepos, eerot, armname='lft')
            # hmn.movearmfk(lftjnts, armname='lft')

            # if rgtjnts is not None and lftjnts is not None: # we are no more checking this, this is already done.
            availablecomfortabletestgoallist.append(testgoalmat)
            graspsforavailablecomfortabletestgoallist.append([besthmngrasprgt, besthmngrasplft])
            #visualize this pose
            availabletestedboardpose = copy.deepcopy(middleboard0)
            availabletestedboardpose.setColor(1,1,0,0.5)
            availabletestedboardpose.setMat(base.pg.np4ToMat4(testgoalmat))
            availabletestedboardpose.reparentTo(base.render)

            # print("Found available human grasp for both arms, its id is ", testgoalid)
        else:
            print("Test goal board pose ", testgoalid ," is not available for both human hands")

    print("Number of comfortable poses for both arms arms is", len(availablecomfortabletestgoallist))

    ### the robot part ###
    #check availability of the comfortable poses to the robot
    rbtavailablebrdgoalslist = []
    for rbttestbrdgoalmat4 in availablecomfortabletestgoallist:
        grasppairsg = sharedgrasp.availableGraspStartGoal("middle", brdmat4upstart, rbttestbrdgoalmat4, armname="lft", isrender=False)
        if len(grasppairsg) > 0:
            # print("returned grasp pair length is ", len(grasppairsg))
            rbtavailablebrdgoalslist.append(rbttestbrdgoalmat4)
            print("A robot reachable pose among the human comfortable poses is found!")

    print("Number of available poses for the robot are, ", len(rbtavailablebrdgoalslist)) #uncomment for debugging

    #rank the reachable poses according to their distance from the goal assembly pose
    distfromassemblylist_ = []
    for brdpose in rbtavailablebrdgoalslist:
        print("brdpose is", repr(brdpose))
        print("brdassemblyposition is", middleboardassemblymat4[:3,3])
        distfromassembly_ = np.linalg.norm(middleboardassemblymat4[:3,3]-brdpose[:3,3])
        distfromassemblylist_.append(distfromassembly_)
        print("dist from assembly is", distfromassembly_)

    nearestgoalposesindces = [distfromassemblylist_.index(x) for x in sorted(distfromassemblylist_)]
    nearestgoalposeindex = nearestgoalposesindces[0]
    farthestgoalposeindex = nearestgoalposesindces[-1]
    # print ("sorted nearest board poses are", sorted(distfromassemblylist_))

    nearestgoalpose = rbtavailablebrdgoalslist[nearestgoalposeindex]
    farthestgoalpose = rbtavailablebrdgoalslist[farthestgoalposeindex]
    print("nearest is", nearestgoalpose, " difference is ", np.linalg.norm(middleboardassemblymat4[:3,3]-nearestgoalpose[:3,3]))
    print("farthest is", farthestgoalpose, " difference is ", np.linalg.norm(middleboardassemblymat4[:3,3]-farthestgoalpose[:3,3]))

    nearestboard = copy.deepcopy(middleboard0)
    nearestboard.setColor(1,0,1,0.5)
    nearestboard.setMat(base.pg.np4ToMat4(nearestgoalpose))
    nearestboard.reparentTo(base.render)

    nearestgrasppair = sharedgrasp.availableGraspStartGoal("middle", brdmat4upstart, nearestgoalpose, armname="lft", isrender=True)

    #get the human eepos, eerot for the nearest pose
    #we need the ranking again of the grasp for the last pose
    iclistrgt = []
    iclistlft = []
    availablehmngraspsrgt = []
    availablehmngraspslft = []

    for idgc, gc in enumerate(premiddle):
        eerot = np.dot(nearestgoalpose[:3, :3], gc[2][:3, :3])
        eepos = np.dot(nearestgoalpose[:3, :3], gc[1]) + nearestgoalpose[:3, 3]
        boardcom = nearestgoalpose[:3, 3]

        # the board center and the cabinet pose
        if np.linalg.norm(boardcom - eepos) < 200:
            rgtjnts = hmn.numik(eepos, eerot, armname='rgt')
            if rgtjnts is not None:
                hmn.movearmfk(rgtjnts, armname='rgt')
                ic = humanik.manipulability_inversecondition(hmn, armname='rgt') * 700
                # print("for the right human hand grasp ", idgc,", its quality ic is ", ic) #uncomment for debugging
                if ic >= 0.4:
                    # save the available grasp
                    availablehmngraspsrgt.append(gc)
                    # save the quality of the available human grasps
                    iclistrgt.append(ic)
                    # their indecies in the original pregrasps
                    rgb = cmap(ic)
                    # hmnmnp = hmnmg.gensnp(hmn, drawhand=True, rgbargthnd=np.array([rgb[0],rgb[1],rgb[2],.5]),rgbalftarm=np.array([255,255,255,0]),rgbalfthnd=np.array([255,255,255,0]))
                    # hmnmnp.reparentTo(base.render)

        #if the left arm is to be considered
        if np.linalg.norm(boardcom - eepos) < 200:
            lftjnts = hmn.numik(eepos, eerot, armname='lft')
            if lftjnts is not None:
                hmn.movearmfk(lftjnts, armname='lft')
                ic = humanik.manipulability_inversecondition(hmn, armname='lft') * 700
                # print("for the left human hand grasp ", idgc,", its quality ic is ", ic) #uncomment for debugging
                if ic >= 0.4:
                    # save the available grasp
                    availablehmngraspslft.append(gc)
                    # save the quality of the available human grasps
                    iclistlft.append(ic)
                    rgb = cmap(ic)
                    # hmnmnp = hmnmg.gensnp(hmn, drawhand=True, rgbalfthnd=np.array([rgb[0],rgb[1],rgb[2],.5]),rgbargtarm=np.array([255,255,255,0]),rgbargthnd=np.array([255,255,255,0]))
                    # hmnmnp.reparentTo(base.render)

    if len(availablehmngraspsrgt) > 0 and len(availablehmngraspslft) > 0:
        iclistindecesrgt = [iclistrgt.index(x) for x in sorted(iclistrgt, reverse=True)]
        bestindexrgt = iclistindecesrgt[0]
        besthmngrasprgt = availablehmngraspsrgt[bestindexrgt]

        eerot = np.dot(nearestgoalpose[:3, :3], besthmngrasprgt[2][:3, :3])
        eepos = np.dot(nearestgoalpose[:3, :3], besthmngrasprgt[1]) + nearestgoalpose[:3, 3]

        rgtjnts = hmn.numik(eepos, eerot, armname='rgt')

        # for the lft arm
        iclistindeceslft = [iclistlft.index(x) for x in sorted(iclistlft, reverse=True)]
        bestindexlft = iclistindeceslft[0]
        besthmngrasplft = availablehmngraspslft[bestindexlft]

        eerot = np.dot(nearestgoalpose[:3, :3], besthmngrasplft[2][:3, :3])
        eepos = np.dot(nearestgoalpose[:3, :3], besthmngrasplft[1]) + nearestgoalpose[:3, 3]
        # nearestgoalpose, bro!!!
        lftjnts = hmn.numik(eepos, eerot, armname='lft')

        # visualize this pose
        # availabletestedboardpose = copy.deepcopy(largeboard0)
        availabletestedboardpose.setColor(1, 1, 0, 0.5)
        availabletestedboardpose.setMat(base.pg.np4ToMat4(nearestgoalpose))
        availabletestedboardpose.reparentTo(base.render)

        # print("Found available human grasp for both arms, its id is ", testgoalid) #uncomment for debugging

        # if both arms
        hmn.movearmfk(rgtjnts, armname='rgt')
        hmn.movearmfk(lftjnts, armname='lft')

        hmnmnp = hmnmg.gensnp(hmn, drawhand=True, rgbargthnd=np.array([0.0, 1.0, 0.0, 1]),
                              rgbalfthnd=np.array([0.0, 1.0, 0.0, 1]))
        hmnmnp.reparentTo(base.render)

        print("The new goal handover pose for step-4 is", repr(nearestgoalpose))


    base.run()
