<h1>Piecewise Function Plotter</h1>

<h2>Overview</h2>

The <strong>Piecewise Function Plotter</strong> is a Python application that uses Tkinter for its graphical user interface (GUI) and Matplotlib for plotting functions. This application allows users to input multiple piecewise functions, specify their intervals, and visualize the combined plot of these functions. The GUI includes features for dynamic input and plotting, as well as a scrollable interface to accommodate a varying number of functions.

<h2>Features</h2>

<ul>
    <li><strong>Dynamic Function Input:</strong> Users can specify any number of piecewise functions and their intervals.</li>
    <li><strong>Scrollable Interface:</strong> A scrollable frame allows users to input multiple functions and their intervals without space constraints.</li>
    <li><strong>Graphical Plotting:</strong> Functions are plotted using Matplotlib with support for repeating segments.</li>
    <li><strong>Function Parsing:</strong> Supports common mathematical functions and constants, including trigonometric functions, logarithms, and square roots.</li>
</ul>

<h2>Installation</h2>

To get started with this project, you'll need Python installed on your system. The application also requires some external libraries which can be installed via <code>pip</code>.

<h3>Clone the Repository</h3>

<pre><code>git clone https://github.com/Alenaak/Graph-Plotter-.git
cd piecewise-function-plotter</code></pre>

<h3>Install Dependencies</h3>

<pre><code>pip install -r requirements.txt</code></pre>

<pre><code># requirements.txt includes:
numpy
sympy
matplotlib</code></pre>

<h2>Usage</h2>

<h3>Run the Application</h3>

<pre><code>python app.py</code></pre>

<h3>Using the GUI</h3>

<ul>
    <li>Enter the number of functions you wish to input.</li>
    <li>For each function, enter the function expression and its corresponding interval (start and end values).</li>
    <li>Click "Set Number of Functions" to generate input fields for each function.</li>
    <li>After entering the function details, click "Plot" to visualize the functions.</li>
</ul>

<h2>Example Inputs</h2>

Here are some example inputs you can use to test the application:

<h3>Intersecting Functions</h3>

<ul>
    <li><strong>Function 1:</strong> <code>x - 1</code>
        <ul>
            <li>Interval Start: <code>-1</code></li>
            <li>Interval End: <code>2</code></li>
        </ul>
    </li>
    <li><strong>Function 2:</strong> <code>-x + 1</code>
        <ul>
            <li>Interval Start: <code>-1</code></li>
            <li>Interval End: <code>2</code></li>
        </ul>
    </li>
</ul>

<h3>General Inputs</h3>

<ul>
    <li><strong>Function 1:</strong> <code>sin(x)</code>
        <ul>
            <li>Interval Start: <code>-π</code></li>
            <li>Interval End: <code>0</code></li>
        </ul>
    </li>
    <li><strong>Function 2:</strong> <code>cos(x)</code>
        <ul>
            <li>Interval Start: <code>0</code></li>
            <li>Interval End: <code>π/2</code></li>
        </ul>
    </li>
    <li><strong>Function 3:</strong> <code>x**2</code>
        <ul>
            <li>Interval Start: <code>π/2</code></li>
            <li>Interval End: <code>π</code></li>
        </ul>
    </li>
</ul>

<h2>Screenshots</h2>




<h3>Example Plot</h3>
<img src="https://github.com/Alenaak/Graph-Plotter-/blob/main/images/1.PNG" alt="Application Interface" width="600"/>
<img src="https://github.com/Alenaak/Graph-Plotter-/blob/main/images/2.PNG" alt="Application Interface" width="600"/>
<img src="https://github.com/Alenaak/Graph-Plotter-/blob/main/images/3.PNG" alt="Application Interface" width="600"/>

<h2>Contributing</h2>

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
    <li>Make your changes.</li>
    <li>Commit your changes (<code>git commit -am 'Add new feature'</code>).</li>
    <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
    <li>Create a new Pull Request.</li>
</ol>

<h2>License</h2>

This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.

<h2>Contact</h2>

If you have any questions or suggestions, feel free to open an issue or contact me directly.
