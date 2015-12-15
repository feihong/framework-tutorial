def setup():
    import sys
    from pathlib2 import Path

    path1 = Path(__file__).parent.parent.parent / 'framehack/interpolate/solutions'
    sys.path.append(str(path1))

    path2 = Path(__file__).parent.parent.parent / 'framehack/wrapper/solutions'
    sys.path.append(str(path2))
