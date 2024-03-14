# Pytools151

Useful debugging tools, my favored implementations, and templates for convenient Python coding.

All the code are written casually during my daily development, and I hope they can be helpful to you as well. It is not a package. Just copy and paste the code you need.

## Analysis

Code here are used to analysis, for example, to measure the runtime using a timer.

<details>
<summary>timer</summary>

Include a `Timer` class that simulates a stopwatch to measure the runtime of your code. It supports `lap` and `refresh` operations. You can log the time each time you lap or sum up the time spent in a certain interval inside a loop. See examples in the code.

</details>


<details>
<summary>searcher</summary>

Include two funny wrappers that catch your error messages and search online through Baidu or StackOverflow.

Added another funny wrappers `aisearch151` that automatically use AI 151 to search online to debug. 

</details>


## Visualization

Code here are used to visualize, for example, make videos from indexed images.

<details>
<summary>video_utils</summary>

Include `video_slice` function to cut video with a certain time interval at a certain fps, and save as frame images.

</details>

<details>
<summary>image_utils</summary>

Include `crop_image` function to crop images with a certain size and save as a video.

</details>

## Template

Template code like cerain tasks, for example, run python code parallelly.

<details>
<summary>parallel</summary>

Include `parallel_run` function to run a function parallelly with a certain number of processes. This function is a good replacement for `for-in-range` if each iteration is independent and time-consuming.

</details>

<details>
<summary>file_helper</summary>

Include `add_to_zip` function to filter and add files to a zip file.

Include `walk_folder` function to walk through a folder and return all files with a certain extension. 

</details>