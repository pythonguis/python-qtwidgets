# Custom Qt5 Python Widgets

Qt5 comes with a huge number of widgets built-in, from simple text boxes to digital displays, vector graphics canvas and a full-blown web browser. While you can build perfectly functional applications with the built-in widgets, sometimes your applications will need something a little *different*.

![Graphical Equalizer](https://i.imgur.com/0F2ZgqE.gif)

This repo is a little collection of custom Python Qt5 widgets I've built myself. They are compatible with both PyQt5 and PySide2 (Qt for Python). Currently the repository includes —

1. **ColorButton** — a single button showing a selected colour. Left-click to change, or right click to reset to `None`. Uses the platform colour selection tool to choose colours.
2. **EqualizerBar** - [a graphical equalizer visualisation](https://www.learnpyqt.com/widgets/equalizerbar/) for displaying audio frequency changes. Customiseable colours and channels.
3. **Gradient** — a gradient editor allowing [creation of complex linear gradients](https://www.learnpyqt.com/widgets/gradient/), with multiple positionable stops.
4. **Paint** — a scribble pad, left-click to draw, right-click to fill. The colours are customizable, try hooking it to the ColorButton or Palette.
5. **Palette** — a [array of colours to choose from](https://www.learnpyqt.com/widgets/palette/), can be arranged horizontally, vertically or in a grid.

For a more detailed introduction to each widget and a walkthrough of their APIs  
see [the custom widget library on LearnPyQt](https://www.learnpyqt.com/widgets/). 

More custom widgets will follow, *if you have ideas just let me know!*

**Licensed MIT/BSDv2** feel free to use in your own projects.