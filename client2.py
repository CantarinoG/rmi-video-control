import flet as ft
import Pyro4
from data import availableVideos, ip

class VideoClientApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.ns = Pyro4.locateNS(host=ip)
        self.videos = []
        self.selected_video = None
        self.load_videos()

    def load_videos(self):
        videos = []
        with Pyro4.locateNS() as ns:
            for video, videoUri in ns.list(prefix="example.video.").items():
                print("found video", video)
                videos.append(Pyro4.Proxy(videoUri))
        if not videos:
            raise ValueError("no videos found! (have you started the servers first?)")
        

    def build(self):
        self.video_buttons = [
            ft.ElevatedButton(
                text=f"VIDEO {i+1}", 
                on_click=lambda e, i=i: self.select_video(i), 
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREEN if i == 0 else ft.colors.BLACK,
                    color=ft.colors.WHITE if i == 0 else ft.colors.GREEN
                )
            ) for i in range(len(self.videos))
        ]

        self.selected_video = 0 if self.videos else None

        return ft.Column(
            [
                ft.Text("CONHEÇA A HISTÓRIA DO", size=20, color=ft.colors.WHITE),
                ft.Text("FUTEBOL", size=50, color=ft.colors.GREEN),
                ft.Row(self.video_buttons, alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                ft.Row(
                    [
                        ft.ElevatedButton(text="PLAY", on_click=self.play_video),
                        ft.ElevatedButton(text="PAUSE", on_click=self.pause_video),
                        ft.ElevatedButton(text="STOP", on_click=self.stop_video)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Text(
                    "Neste vídeo abordamos a importância do jogo de futebol, e como surgiu a ideia e o primeiro jogo",
                    size=16,
                    color=ft.colors.WHITE,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

    def select_video(self, index):
        self.selected_video = index
        for i, button in enumerate(self.video_buttons):
            if i == index:
                button.bgcolor = ft.colors.GREEN
                button.color = ft.colors.WHITE
            else:
                button.bgcolor = ft.colors.BLACK
                button.color = ft.colors.GREEN
        self.update()

    def play_video(self, e):
        if self.selected_video is not None:
            self.videos[self.selected_video].play()

    def pause_video(self, e):
        if self.selected_video is not None:
            self.videos[self.selected_video].pause()

    def stop_video(self, e):
        if self.selected_video is not None:
            self.videos[self.selected_video].stop()

def main(page: ft.Page):
    page.title = "História do Futebol"
    
    page.bgcolor = ft.colors.WHITE
    
   
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.RAILWAY_ALERT_ROUNDED),
        leading_width=40,
        title=ft.Text("HISTÓRIA DO FUTEBOL"),
        center_title=False,
        bgcolor=ft.colors.GREY_500,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
   
    
    
    image = ft.Container(
        expand=2,
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.GREEN_100, ft.colors.GREEN],    
        ),
        content=ft.Image(
            src='https://images.vexels.com/content/249473/preview/soccer-player-sport-character-eed4f9.png',
            scale=ft.Scale(scale=1.6),
            width=500,
            
        )
    )
    info = ft.Container(
        expand=3,
        padding=ft.padding.all(30),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='VIDEO 1', color=ft.colors.GREEN),
                ft.Text(
                    value='História',
                    weight=ft.FontWeight.BOLD,
                    size=20,
                    color=ft.colors.BLACK,
                ),
                ft.Text(
                    value='A historia do futebol é chata e mais chato é assistir',
                    color=ft.colors.GREY,
                    text_align=ft.TextAlign.CENTER,
                )
            ]
        )
    )
    players = ft.Container(
        expand=1,
        bgcolor=ft.colors.GREEN,
        border_radius=ft.border_radius.vertical(bottom=20),
        padding=ft.padding.symmetric(horizontal=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            name=ft.icons.PLAY_ARROW,
                            color=ft.colors.WHITE,
                            size=20,
                        ),
                        ft.Text(
                            value='PLAY',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),
                
                ft.VerticalDivider(opacity=0.5),
                
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            name=ft.icons.PAUSE,
                            color=ft.colors.WHITE,
                            size=20,
                        ),
                        ft.Text(
                            value='PAUSE',
                            color=ft.colors.WHITE,
                        )
                    ]
                ),
                
                ft.VerticalDivider(opacity=0.5),
                
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            name=ft.icons.STOP,
                            color=ft.colors.WHITE,
                            size=20,
                        ),
                        ft.Text(
                            value='STOP',
                            color=ft.colors.WHITE,
                        )
                    ]
                )
            ]    
        ),
    )
    
    layout = ft.Container(
        height=400,
        width=250,
        shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.GREY),
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                players,
            ]
        )
    )
    
    page.add(layout)
    

    
ft.app(target=main)
