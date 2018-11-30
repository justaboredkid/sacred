# Sacred
ASCII art import. IN PYTHON. All you need to do is to grab some ascii art (from the web or somewhere else), convert it into json (using ./asciigen.py), and:
```
import sacred

scene = sacred.Scene()

scene.obj("test.json", 5, 10)
scene.render()
```

*Documentation will be here soon.*
