MultiCode - A Multi-Instance VSCode manager
=============================
## About
MultiCode allows you to have multiple, independent instances of VSCode next to each other for different purposes.  
MultiCode is written in pure Python and is therefore cross-platform. Currently only Linux and Windows are supported. MacOS support will be added in the near future.

## Installation

### Get this repository
Clone this repository using git:  
<pre><code>git clone https://github.com/Nastygamer/MultiCode</code></pre>
Or download it as a zip:
https://github.com/NastyGamer/MultiCode/archive/master.zip  

### Install the requirements  
head into the repository:  
<pre><code>cd MultiCode</pre></code>
and install the requirements:  
<pre><code>pip install -r requirements.txt</pre></code>

## Usage  
### List installed instances  
<pre><code>python3 MultiCode.py list</pre></code>
Running it might return something like this:  
<pre><code>Name       → LaTeX
Created    → 24.04.2020
Last Used  → 1.1.2000

Name       → Java
Created    → 24.04.2020
Last Used  → 24.04.2020

Name       → Markdown
Created    → 24.04.2020
Last Used  → 1.1.2000</pre></code>

### Creating a new instance
<pre><code>python3 MultiCode.py create</pre></code>  
You will be prompted to enter a name for the new instance  

### Running an instance
<pre><code>python3 MultiCode.py run</pre></code>
You will be prompted to enter the name of the instance to run

### Deleting an instance
<pre><code>python3 MultiCode.py delete</pre></code>  
You will be prompted to enter the name of the instance to be deleted




