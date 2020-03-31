# Custom Qt5 Python Widgets

Qt5 comes with a huge number of widgets built-in, from simple text boxes to digital displays, vector graphics canvas and a full-blown web browser. While you can build perfectly functional applications with the built-in widgets, sometimes your applications will need a *more*.

This repo contains a library of [custom Python Qt5 widgets](https://www.learnpyqt.com/widgets/) which are free to use in your own applications. Widgets are compatible with both PyQt5 and PySide2 (Qt for Python). Currently the repository includes -

| Widgets | Library |
| :---: | :---: |
| ![Graphical Equalizer](https://i.imgur.com/0F2ZgqE.gif)<br>**Graphical Equalizer**<br>Visualize audio frequency changes with configurable styles and decay<br>`from qtwidgets import EqualizerBar`<br>[Documentation](https://www.learnpyqt.com/widgets/equalizerbar/) | ![Power Meter](https://i.imgur.com/0dpZIMV.gif)<br>**Power Bar**<br>Rotary control with amplitude display<br>`from qtwidgets import PowerBar`<br>[Documentation](https://www.learnpyqt.com/courses/custom-widgets/creating-your-own-custom-widgets/)  |
| ![Palette](https://cdn.learnpyqt.com/media/images/Screenshot_2019-06-15_at_15.18.14.max-500x500.png)<br>**Palette**<br>Select colours from a configurable linear or grid palette.<br>`from qtwidgets import PaletteHorizontal`<br>`from qtwidgets import PaletteGrid`<br>[Documentation](https://www.learnpyqt.com/widgets/palette/) | ![Gradient Editor](https://cdn.learnpyqt.com/media/images/Screenshot_2019-06-15_at_18.32.52.max-500x500.png)<br>**Linear Gradient Editor**<br>Design custom linear gradients with multiple stops and colours.<br>`from qtwidgets import Gradient`<br>[Documentation](https://www.learnpyqt.com/widgets/gradient/)|
| **Color Button**<br>Simple button that displays and selects colours.<br>`from qtwidgets import ColorButton` | **Paint**<br>Draw pictures with a custom bitmap canvas, with colour and pen control.<br>`from qtwidgets import Paint` |
| **Password Edit**<br>A password line editor with toggleable visibility action.<br>`from qtwidgets import PasswordEdit` | |

For a more detailed introduction to each widget and a walkthrough of their APIs  
see [the custom widget library on LearnPyQt](https://www.learnpyqt.com/widgets/). 

More custom widgets will follow, *if you have ideas just let me know!*

**Licensed MIT/BSDv2** feel free to use in your own projects.
