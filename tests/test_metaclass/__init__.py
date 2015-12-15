def setup():
    # import sys, os
    # from os import path as op
    # sys.path.append(op.join(op.dirname(__file__), '..', '..', 'Metaclass'))
    import sys
    from pathlib2 import Path

    path1 = Path(__file__).parent.parent.parent / 'metaclass/bitfield/solutions'
    sys.path.append(str(path1))
