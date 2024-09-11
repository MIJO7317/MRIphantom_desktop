from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
import numpy as np
import plotly.graph_objects as go
from scipy.spatial import cKDTree


class Scatter3D(QWidget):
    """
    Class for 3D scatter viewer
    """

    def __init__(self, data_ct, data_mri, voxel_size, z_spacing, title="3D просмотр отклонений"):
        super().__init__()

        self.fig = None

        self.data_ct = data_ct
        self.data_mri = data_mri

        self.voxel_size = voxel_size
        self.z_spacing = z_spacing

        self.setWindowTitle(title)

        self.browser = QWebEngineView(self)

        # Add table
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.browser)

        self.resize(1200, 800)

        self.init_scatter3d()
        self.browser.reload()

    def init_scatter3d(self, max_deviation=2):
        """
        Initialize 3D scatter viewer
        """

        self.fig = go.Figure().update_layout(template="plotly_white")

        coords_mr = np.array(self.data_mri)
        coords_ct = np.array(self.data_ct)

        # Инициализация списков для 3D точек и их отклонений для Plotly
        mr_x, mr_y, mr_z = [], [], []
        ct_x, ct_y, ct_z = [], [], []
        dev_x, dev_y, dev_z, dev_colors = [], [], [], []

        # Проходим через каждый срез
        for z, (slice_mr, slice_ct) in enumerate(zip(coords_mr, coords_ct)):
            mr_points = np.array(slice_mr)
            ct_points = np.array(slice_ct)

            # Фильтрация NaN значений
            valid_mr = ~np.isnan(mr_points).any(axis=1)
            valid_ct = ~np.isnan(ct_points).any(axis=1)
            valid_points = valid_mr & valid_ct

            mr_points = mr_points[valid_points]
            ct_points = ct_points[valid_points]

            if len(mr_points) == 0 or len(ct_points) == 0:
                continue  # Пропускаем срез, если все точки были NaN

            # Создаем KD-дерево для поиска ближайших соседей
            tree = cKDTree(ct_points)
            distances, indices = tree.query(mr_points)

            # Переупорядочиваем точки CT, чтобы они соответствовали ближайшим точкам MR
            ct_points = ct_points[indices]

            deviations = np.linalg.norm(mr_points - ct_points, axis=1)

            # Добавляем точки в списки для Plotly
            mr_x.extend(mr_points[:, 0])
            mr_y.extend(mr_points[:, 1])
            mr_z.extend([z] * len(mr_points))

            ct_x.extend(ct_points[:, 0])
            ct_y.extend(ct_points[:, 1])
            ct_z.extend([z] * len(ct_points))

            dev_x.extend(ct_points[:, 0])
            dev_y.extend(ct_points[:, 1])
            dev_z.extend([z] * len(ct_points))
            dev_colors.extend(deviations)

            # Add deviation points with a color bar and adjusted color scale
        self.fig.add_trace(
            go.Scatter3d(
                x=dev_x,
                y=dev_y,
                z=dev_z,
                mode="markers",
                marker=dict(
                    size=3,
                    color=dev_colors,
                    colorscale="YlOrRd",  # Use a warm color scale
                    cmin=0,
                    cmax=max_deviation,
                    colorbar=dict(
                        title="Отклонение",  # Add units to the colorbar title
                        tickvals=[i for i in range(max_deviation + 1)],
                        ticktext=[f"{i}" for i in range(max_deviation + 1)],
                    ),
                ),
                name="Отклонения",
                hovertemplate="X: %{x:.2f}<br>Y: %{y:.2f}<br>Срез: %{z:.2f}<br>Отклонение: %{marker.color:.2f}<extra></extra>"
            )
        )

        # Add MR points with a slight transparency for a 3D effect
        self.fig.add_trace(
            go.Scatter3d(
                x=mr_x,
                y=mr_y,
                z=mr_z,
                mode="markers",
                marker=dict(size=3, color="red", opacity=0.8),
                name="МРТ",
            )
        )

        # Add CT points with a slight transparency for a 3D effect
        self.fig.add_trace(
            go.Scatter3d(
                x=ct_x,
                y=ct_y,
                z=ct_z,
                mode="markers",
                marker=dict(size=3, color="blue", opacity=0.8),
                name="КТ",
            )
        )

        # Update layout for better aesthetics and a clean medical look
        self.fig.update_layout(
            title="3D визуализация МРТ и КТ стержней",
            scene=dict(
                aspectratio=dict(x=1,
                                 y=1,
                                 z=self.z_spacing
                                 ),  # Stretch z-axis
                xaxis_title="X",  # Add units to axis titles
                yaxis_title="Y",
                zaxis_title="Z",
                bgcolor="white",  # Set background color to white
            ),
            legend=dict(
                x=0.8,
                y=0.9,
                bgcolor="rgba(255, 255, 255, 0.8)",  # Adjust legend background transparency
                bordercolor="rgba(0, 0, 0, 0.5)",
                borderwidth=2
            ),
            font=dict(family="Arial", size=12),  # Use a clean and readable font
            margin=dict(l=0, r=0, b=0, t=40),  # Reduce margins for a cleaner look
        )

        self.browser.setHtml(self.fig.to_html(include_plotlyjs="cdn"))
