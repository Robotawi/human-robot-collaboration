def boardGrasps(board):
    from manipulation.grip.humanhand import hhdw
    hhdw = hhdw.HHdwFactory()
    rgthmhnd = hhdw.genHand()

    if board == 'middle' or board == 'small':
        premiddle = []
        premiddle.append(rgthmhnd.approachAt(-150, 73, 5, 0, 0, 1, 1, 0, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, 0, 5, 0, 0, 1, 1, 0, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, -73, 5, 0, 0, 1, 1, 0, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-150,73, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150,0, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150,-73, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(150, 73, 5, 0, 0, 1, -1, 0, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, 0, 5, 0, 0, 1, -1, 0, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, -73, 5, 0, 0, 1, -1, 0, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-150, -73, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, 0, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, 73, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, 110, 5, 0, 0, 1, 0, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, 1, 0, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, 110, 5, 0, 0, 1, 0, -1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, 110, 5, 0, 0, -1, 0, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, -1, 0, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, 110, 5, 0, 0, -1, 0, -1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, -110, 5, 0, 0, 1, 0, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, -110, 5, 0, 0, 1, 0, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, -110, 5, 0, 0, 1, 0, 1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, -110, 5, 0, 0, -1, 0, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, -110, 5, 0, 0, -1, 0, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, -110, 5, 0, 0, -1, 0, 1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-150, 73 ,5, 0, 0, 1, 1, .5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, 0 ,5, 0, 0, 1, 1, .5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, -73,5, 0, 0, 1, 1, .5, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-150, 73, 5, 0, 0, -1, 1, .5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, 0, 5, 0, 0, -1, 1, .5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, -73, 5, 0, 0, -1, 1, .5, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(150, 73, 5, 0, 0, 1, -1, .5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, 0, 5, 0, 0, 1, -1, .5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, -73, 5, 0, 0, 1, -1, .5, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(150, 73, 5, 0, 0, -1, -1, .5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, 0, 5, 0, 0, -1, -0.5, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, -73, 5, 0, 0, -1, -1, .5, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, 110, 5, 0, 0, 1, -0.5, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, 1, -0.5, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, 110, 5, 0, 0, 1, -0.5, -1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, 110, 5, 0, 0, -1, -0.5, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, -1, -0.5, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, 110, 5, 0, 0, -1, -0.5, -1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, -110, 5, 0, 0, 1, -0.5, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt( 0, -110, 5, 0, 0, 1, -0.5, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, -110, 5, 0, 0, 1, -0.5, 1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, -110, 5, 0, 0, -1, -0.5, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, -110, 5, 0, 0, -1, -0.5, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt( 100, -110, 5, 0, 0, -1, -0.5, 1, 0, jawwidth=60))

        # -30 is done
        premiddle.append(rgthmhnd.approachAt(-150, -73, 5, 0, 0, 1, 1, -.5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, 0, 5, 0, 0, 1, 1, -.5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, 73, 5, 0, 0, 1, 1, -.5, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-150, 73, 5, 0, 0, -1, 1, -.5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, 0, 5, 0, 0, -1, 1, -.5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(-150, -73, 5, 0, 0, -1, 1, -.5, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(150, 73, 5, 0, 0, 1, -1, -.5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, 0, 5, 0, 0, 1, -1, -.5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, -73, 5, 0, 0, 1, -1, -.5, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(150, 73, 5, 0, 0, -1, -1, -.5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, 0, 5, 0, 0, -1, -1, -0.5, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(150, -73, 5, 0, 0, -1, -1, -.5, 0, jawwidth=60))


        premiddle.append(rgthmhnd.approachAt(-100, 110, 5, 0, 0, 1, 0.5, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, 1, 0.5, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, 110, 5, 0, 0, 1, 0.5, -1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, 110, 5, 0, 0, -1, 0.5, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, -1, 0.5, -1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, 110, 5, 0, 0, -1, 0.5, -1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, -110, 5, 0, 0, 1, 0.5, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, -110, 5, 0, 0, 1, 0.5, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, -110, 5, 0, 0, 1, 0.5, 1, 0, jawwidth=60))

        premiddle.append(rgthmhnd.approachAt(-100, -110, 5, 0, 0, -1, 0.5, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(0, -110, 5, 0, 0, -1, 0.5, 1, 0, jawwidth=60))
        premiddle.append(rgthmhnd.approachAt(100, -110, 5, 0, 0, -1, 0.5, 1, 0, jawwidth=60))

        return premiddle

    if board == 'large':
        prelarge = []

        prelarge.append(rgthmhnd.approachAt(-255, 73, 5, 0, 0, 1, 1, 0, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, 0, 5, 0, 0, 1, 1, 0, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, -73, 5, 0, 0, 1, 1, 0, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-255,73, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255,0, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255,-73, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(255, 73, 5, 0, 0, 1, -1, 0, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(255, 0, 5, 0, 0, 1, -1, 0, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(255, -73, 5, 0, 0, 1, -1, 0, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-255, -73, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, 0, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, 73, 5, 0, 0, -1, 1, 0, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-145, 110, 5, 0, 0, 1, 0, -1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, 1, 0, -1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(145, 110, 5, 0, 0, 1, 0, -1, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-145, 110, 5, 0, 0, -1, 0, -1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, -1, 0, -1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(145, 110, 5, 0, 0, -1, 0, -1, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-145, -110, 5, 0, 0, 1, 0, 1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(0, -110, 5, 0, 0, 1, 0, 1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(145, -110, 5, 0, 0, 1, 0, 1, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-145, -110, 5, 0, 0, -1, 0, 1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(0, -110, 5, 0, 0, -1, 0, 1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(145, -110, 5, 0, 0, -1, 0, 1, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-255, 73 ,5, 0, 0, 1, 1, .5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, 0 ,5, 0, 0, 1, 1, .5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, -73,5, 0, 0, 1, 1, .5, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-255, 73, 5, 0, 0, -1, 1, .5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, 0, 5, 0, 0, -1, 1, .5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, -73, 5, 0, 0, -1, 1, .5, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(255, 73, 5, 0, 0, 1, -1, .5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(255, 0, 5, 0, 0, 1, -1, .5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(255, -73, 5, 0, 0, 1, -1, .5, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(255, 73, 5, 0, 0, -1, -1, .5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(255, 0, 5, 0, 0, -1, -0.5, 1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(255, -73, 5, 0, 0, -1, -1, .5, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-145, 110, 5, 0, 0, 1, -0.5, -1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, 1, -0.5, -1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(145, 110, 5, 0, 0, 1, -0.5, -1, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-145, 110, 5, 0, 0, -1, -0.5, -1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(0, 110, 5, 0, 0, -1, -0.5, -1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(145, 110, 5, 0, 0, -1, -0.5, -1, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-145, -110, 5, 0, 0, 1, -0.5, 1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt( 0, -110, 5, 0, 0, 1, -0.5, 1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(145, -110, 5, 0, 0, 1, -0.5, 1, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-145, -110, 5, 0, 0, -1, -0.5, 1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(0, -110, 5, 0, 0, -1, -0.5, 1, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt( 145, -110, 5, 0, 0, -1, -0.5, 1, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-255, -73, 5, 0, 0, 1, 1, -.5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, 0, 5, 0, 0, 1, 1, -.5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, 73, 5, 0, 0, 1, 1, -.5, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(-255, 73, 5, 0, 0, -1, 1, -.5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, 0, 5, 0, 0, -1, 1, -.5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(-255, -73, 5, 0, 0, -1, 1, -.5, 0, jawwidth=60))

        prelarge.append(rgthmhnd.approachAt(255, 73, 5, 0, 0, 1, -1, -.5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(255, 0, 5, 0, 0, 1, -1, -.5, 0, jawwidth=60))
        prelarge.append(rgthmhnd.approachAt(255, -73, 5, 0, 0, 1, -1, -.5, 0, jawwidth=60))
        return prelarge
