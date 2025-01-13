import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Function to create a rotation matrix for a given angle in radians
def rotation_matrix(angle):
    """Return a 2D rotation matrix for a given angle in radians."""
    return np.array([[np.cos(angle), -np.sin(angle)],
                     [np.sin(angle), np.cos(angle)]])

# Function to draw the bicycle
def draw_bicycle(ax, scale=1, translate=(0, 0), rotation=0):
    # Parameters for the bicycle components
    wheel_radius = 1
    frame_length = 3
    frame_height = 1
    handlebar_length = 1.5
    pedal_radius = 0.1
    
    # Draw the wheels
    wheel1 = plt.Circle((0, 0), wheel_radius * scale, edgecolor='black', facecolor='none', lw=2)
    wheel2 = plt.Circle((frame_length, 0), wheel_radius * scale, edgecolor='black', facecolor='none', lw=2)
    
    ax.add_patch(wheel1)
    ax.add_patch(wheel2)
    
    # Draw the frame
    ax.plot([0, frame_length], [0, 0], color='black', lw=2)  # bottom frame (horizontal)
    ax.plot([0, frame_length / 2], [0, frame_height * scale], color='black', lw=2)  # front frame (diagonal)
    ax.plot([frame_length / 2, frame_length], [frame_height * scale, 0], color='black', lw=2)  # back frame (diagonal)
    
    # Draw the handlebars (vertical line)
    ax.plot([frame_length / 2, frame_length / 2], [frame_height * scale, frame_height * scale + handlebar_length * scale], color='black', lw=2)
    
    # Draw the pedals (small circles in the center of the wheels)
    ax.plot([frame_length / 2], [0], 'ko', markersize=5)  # Pedal at the center of wheel1
    
    # Apply scaling, rotation, and translation to all the components
    components = [wheel1, wheel2]
    for comp in components:
        comp.set_radius(comp.get_radius() * scale)
    
    # Rotate the bicycle
    for element in ax.collections:
        for path in element.get_paths():
            path.vertices = np.dot(path.vertices, rotation_matrix(rotation))
    
    # Translate the entire bicycle
    ax.set_xlim(ax.get_xlim()[0] + translate[0], ax.get_xlim()[1] + translate[0])
    ax.set_ylim(ax.get_ylim()[0] + translate[1], ax.get_ylim()[1] + translate[1])

# Animation function to update the bicycle's position and wheel rotation
def update(frame, ax, wheel1, wheel2, line, scale_factor, wheel_radius, frame_length):
    # Apply translation to simulate movement
    translate_x = frame * 0.1  # Moving the bicycle horizontally
    translate_y = 0  # No vertical movement
    
    # Apply rotation to simulate wheel rotation
    rotation_angle = frame * 0.1  # Rotating the wheel for movement simulation
    
    # Update the translation and rotation of the bicycle
    ax.clear()
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Draw the bicycle with updated transformations
    draw_bicycle(ax, scale=scale_factor, translate=(translate_x, translate_y), rotation=rotation_angle)
    
    return []

# Main function to create the plot
def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Parameters for transformations
    scale_factor = 1  # Scaling factor (no scaling for simplicity)
    wheel_radius = 1  # Wheel radius
    frame_length = 3  # Frame length

    # Set the number of frames for the animation
    frames = 100
    ani = FuncAnimation(fig, update, frames=frames, fargs=(ax, None, None, None, scale_factor, wheel_radius, frame_length), interval=50)

    plt.show()

if __name__ == "__main__":
    main()