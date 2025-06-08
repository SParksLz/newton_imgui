import warp as wp
import warp.render
import newton.utils.render
from newton.utils.render import CreateSimRenderer

import imgui
from imgui.integrations.pyglet import create_renderer

# renderer = warp.render.OpenGLRenderer

class SimpleInspector :
    def __init__(self, window):
        imgui.create_context()
        imgui.get_io().display_size = 100, 100
        imgui.get_io().fonts.get_tex_data_as_rgba32()

        self.impl = create_renderer(window)

    def update(self):
        imgui.new_frame()

        imgui.begin("Model Inspector", True)
        imgui.text("test")
        # change, values = imgui.v_slider_int(
        value = 55
        change, values = imgui.slider_int(
            "vertical slider int",
            value, 0, 100,
            format = "%d"
        )
        imgui.end()


class SparksRenderer(wp.render.OpenGLRenderer) :
    def __init__(
            self,
            title="Warp",
            scaling=1.0,
            fps=60,
            up_axis="Y",
            screen_width=1024,
            screen_height=768,
            near_plane=1.0,
            far_plane=100.0,
            camera_fov=45.0,
            camera_pos=(0.0, 2.0, 10.0),
            camera_front=(0.0, 0.0, -1.0),
            camera_up=(0.0, 1.0, 0.0),
            background_color=(0.53, 0.8, 0.92),
            draw_grid=True,
            draw_sky=True,
            draw_axis=True,
            show_info=True,
            render_wireframe=False,
            render_depth=False,
            axis_scale=1.0,
            vsync=False,
            headless=None,
            enable_backface_culling=True,
            enable_mouse_interaction=True,
            enable_keyboard_interaction=True,
            device=None,
        ):
        super().__init__(
            title=title,
            scaling=scaling,
            fps=fps,
            up_axis=up_axis,
            screen_width=screen_width,
            screen_height=screen_height,
            near_plane=near_plane,
            far_plane=far_plane,
            camera_fov=camera_fov,
            camera_pos=camera_pos,
            camera_front=camera_front,
            camera_up=camera_up,
            background_color=background_color,
            draw_grid=draw_grid,
            draw_sky=draw_sky,
            draw_axis=draw_axis,
            show_info=show_info,
            render_wireframe=render_wireframe,
            render_depth=render_depth,
            axis_scale=axis_scale,
            vsync=vsync,
            headless=headless,
            enable_backface_culling=enable_backface_culling,
            enable_mouse_interaction=enable_mouse_interaction,
            enable_keyboard_interaction=enable_keyboard_interaction,
            device=device,
        )
        self.inspector = SimpleInspector(self.window)

    def _draw(self):
        self.inspector.update()
        super()._draw()
        imgui.render()
        self.inspector.impl.render(imgui.get_draw_data())


class SimRendererNewOpenGL(CreateSimRenderer(renderer=SparksRenderer)):
    """
    Real-time OpenGL renderer for Newton Physics simulations.

    This renderer provides real-time visualization of physics simulations using
    OpenGL, with interactive camera controls and various rendering options.

    Args:
        model (newton.Model): The Newton physics model to render.
        path (str): Window title for the OpenGL window.
        scaling (float, optional): Scaling factor for the rendered objects.
            Defaults to 1.0.
        fps (int, optional): Target frames per second. Defaults to 60.
        up_axis (newton.AxisType, optional): Up axis for the scene. If None,
            uses model's up axis.
        show_rigid_contact_points (bool, optional): Whether to show contact
            points. Defaults to False.
        contact_points_radius (float, optional): Radius of contact point
            spheres. Defaults to 1e-3.
        show_joints (bool, optional): Whether to show joint visualizations.
            Defaults to False.
        **render_kwargs: Additional arguments passed to the underlying
            OpenGLRenderer.

    Example:
        .. code-block:: python

            import newton

            model = newton.Model()  # your model setup
            renderer = newton.utils.SimRendererOpenGL(model, "Newton Simulator")
            # In your simulation loop:
            renderer.begin_frame(time)
            renderer.render(state)
            renderer.end_frame()

    Note:
        Keyboard shortcuts available during rendering:

        - W, A, S, D (or arrow keys) + mouse: FPS-style camera movement
        - X: Toggle wireframe rendering
        - B: Toggle backface culling
        - C: Toggle coordinate system axes
        - G: Toggle ground grid
        - T: Toggle depth rendering
        - I: Toggle info text
        - SPACE: Pause/continue simulation
        - TAB: Skip rendering (background simulation)
    """

    pass

