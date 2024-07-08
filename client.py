import flet as ft
import Pyro4
from data import availableVideos, video_data_list, integrantes, ip

def create_video_card(video, video_data, theme):
    colors = {
        "light": {
            "card_bg": ft.colors.WHITE,
            "text_title": ft.colors.BLACK,
            "text_subtitle": ft.colors.GREY,
            "button_bg": ft.colors.GREEN,
            "button_text": ft.colors.WHITE,
            "icon_color": ft.colors.BLACK,
        },
        "dark": {
            "card_bg": ft.colors.GREY_900,
            "text_title": ft.colors.WHITE,
            "text_subtitle": ft.colors.GREEN,
            "button_bg": ft.colors.GREEN,
            "button_text": ft.colors.WHITE,
            "icon_color": ft.colors.WHITE,
        },
    }
    
    theme_colors = colors[theme]
    
    image = ft.Container(
        expand=2,
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BLACK, ft.colors.GREEN],    
        ),
        content=ft.Image(
            src=video_data["image"],
            scale=ft.Scale(scale=1.6),
            width=500,
        )
    )
    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value=video_data["title"], color=theme_colors["text_title"]),
                ft.Text(
                    value=video.getName(),
                    weight=ft.FontWeight.BOLD,
                    size=20,
                    color=theme_colors["text_title"],
                ),
                ft.Text(
                    value=video_data["description"],
                    color=theme_colors["text_subtitle"],
                    text_align=ft.TextAlign.CENTER,
                    max_lines=3,
                    overflow=ft.TextOverflow.ELLIPSIS,
                )
            ]
        )
    )
    players = ft.Container(
        expand=1,
        bgcolor=theme_colors["button_bg"],
        border_radius=ft.border_radius.vertical(bottom=20),
        padding=ft.padding.symmetric(horizontal=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.PLAY_ARROW,
                            icon_size=20,
                            icon_color=theme_colors["button_text"],
                            on_click=lambda e: video.play(),
                        ),
                        ft.Text(
                            value='PLAY',
                            color=theme_colors["button_text"],
                        )
                    ]
                ),
                
                ft.VerticalDivider(opacity=0.2),
                
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.PAUSE,
                            icon_size=20,
                            icon_color=theme_colors["button_text"],
                            on_click=lambda e: video.pause(),
                        ),
                        ft.Text(
                            value='PAUSE',
                            color=theme_colors["button_text"],
                        )
                    ]
                ),
                
                ft.VerticalDivider(opacity=0.2),
                
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.STOP,
                            icon_size=20,
                            icon_color=theme_colors["button_text"],
                            on_click=lambda e: video.stop(),
                        ),
                        ft.Text(
                            value='STOP',
                            color=theme_colors["button_text"],
                        )
                    ]
                )
            ]    
        ),
    )
    
    layout = ft.Container(
        height=400,
        width=250,
        shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.GREY),
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.all(30),
        bgcolor=theme_colors["card_bg"],
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                players,
            ]
        )
    )
    
    return layout

def main(page: ft.Page):
    theme = "light"
    
    def switch_theme(e):
        nonlocal theme
        theme = "dark" if theme == "light" else "light"
        page.clean()
        create_ui(page)
    
    def create_ui(page):
        page.title = "História do Futebol"
        page.bgcolor = ft.colors.WHITE if theme == "light" else ft.colors.BLACK
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window_max_width = 1100
        page.window_max_height = 1000
        page.scroll = ft.ScrollMode.AUTO

        navbar = ft.Container(
            width=500,
            height=50,
            border_radius=ft.border_radius.all(20),
            padding=ft.padding.all(5),
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=[ft.colors.GREEN_800, ft.colors.GREEN],    
            ),
            content=ft.Row(
                controls=[
                    ft.Text(
                        value='HISTÓRIA DO FUTEBOL',
                        color=ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.ElevatedButton(
                        text='VÍDEOS',
                        bgcolor=ft.colors.GREEN,
                        color=ft.colors.WHITE,  
                    ),
                    ft.ElevatedButton(
                        text='HISTÓRIA',
                        bgcolor=ft.colors.GREEN,
                        color=ft.colors.WHITE,  
                    ),
                    ft.IconButton(
                        icon=ft.icons.BRIGHTNESS_6,
                        icon_color=ft.colors.WHITE,
                        on_click=switch_theme,
                    )
                ]
            ),
        )

        textTitle = ft.Container(
            padding=ft.padding.all(30),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                controls=[
                    ft.Text(
                        value='CONHEÇA A HISTÓRIA DO', 
                        color=ft.colors.BLACK if theme == "light" else ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                        size=20,
                    ),
                    ft.ShaderMask(
                        content=ft.Text(
                            value='FUTEBOL',
                            weight=ft.FontWeight.BOLD,
                            size=100,
                            color=ft.colors.GREEN,
                        ),
                        shader=ft.LinearGradient(
                            colors=[ft.colors.GREEN_300, ft.colors.GREEN_700],
                        )
                    ),
                    ft.Text(
                        value='Assista aos vídeos abaixo para conhecer a fantástica e maravilhosa história do futebol.',
                        color=ft.colors.BLACK87 if theme == "light" else ft.colors.WHITE70,
                    ),
                ]
            )
        )
        
        textParagraph = ft.Container(
            padding=ft.padding.all(30),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        text_align=ft.TextAlign.JUSTIFY,
                        color=ft.colors.BLACK if theme == "light" else ft.colors.WHITE,
                        spans=[
                            ft.TextSpan(
                                text='UM POUCO SOBRE O FUTEBOL \n\n',
                                style=ft.TextStyle(
                                    size=20,  
                                    weight=ft.FontWeight.BOLD
                                ),
                            ),
                            ft.TextSpan(
                                text="O futebol, conhecido como o esporte das multidões, tem uma história rica e fascinante que remonta ao século XIX. Originado na Inglaterra, rapidamente se tornou um fenômeno mundial, conquistando corações e mentes em todos os continentes. O esporte evoluiu de jogos rudimentares jogados em escolas e campos abertos para uma disciplina altamente organizada e profissionalizada. As primeiras regras oficiais do futebol foram estabelecidas em 1863 pela Football Association, marcando o nascimento do futebol moderno. Desde então, o futebol cresceu exponencialmente, com a criação de competições globais como a Copa do Mundo da FIFA, que é realizada a cada quatro anos e reúne seleções nacionais de todo o planeta. Além disso, clubes históricos como Real Madrid, Barcelona, Manchester United e muitos outros ajudaram a solidificar o status do futebol como o esporte mais popular do mundo. A paixão pelo futebol transcende barreiras culturais e linguísticas, unindo pessoas de diferentes origens em uma celebração coletiva de habilidade, estratégia e espírito esportivo."
                            )
                        ]
                    )
                ]
            )
        )

        textGroup = ft.Container(
            padding=ft.padding.all(30),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.START,
                spacing=0,
                controls=[
                    ft.Text(
                        text_align=ft.TextAlign.CENTER,
                        spans=[
                            ft.TextSpan(text='INTEGRANTES DO GRUPO', style=ft.TextStyle(color=ft.colors.BLACK if theme == "light" else ft.colors.WHITE, weight=ft.FontWeight.BOLD, size=20)),
                        ],
                    ),
                ]
            )
        )

        def create_integrante_context_menu(integrante):
            return ft.CupertinoContextMenu(
                enable_haptic_feedback=True,
                content=ft.Container(
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(integrante["image"], border_radius=ft.border_radius.all(1000), height=100),
                        ]
                    )
                ),
                actions=[
                    ft.CupertinoContextMenuAction(
                        text=integrante['name'],
                        trailing_icon=ft.icons.PERSON,
                        on_click=lambda e: print(f"GitHub: {integrante['github']}"),
                    ),
                    ft.CupertinoContextMenuAction(
                        text=f"GitHub: {integrante['github']}",
                        trailing_icon=ft.icons.WEB,
                        on_click=lambda e: print(f"GitHub: {integrante['github']}"),
                    ),
                    ft.CupertinoContextMenuAction(
                        text=f"Matrícula: {integrante['matricula']}",
                        trailing_icon=ft.icons.CONTACT_PAGE,
                        on_click=lambda e: print(f"Matrícula: {integrante['matricula']}"),
                    ),
                ],
            )

        integrantes_cards = [create_integrante_context_menu(integrante) for integrante in integrantes]
        
        footer = ft.Container(
            padding=ft.padding.all(20),
             gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=[ft.colors.GREEN_800, ft.colors.GREEN],    
            ),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.Text(
                        value="Referências",
                        color=ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.IconButton(
                        icon=ft.icons.LINK,
                        icon_color=ft.colors.WHITE,
                        on_click=lambda e: print("Link para site de referência 1"),
                    ),
                    ft.IconButton(
                        icon=ft.icons.LINK,
                        icon_color=ft.colors.WHITE,
                        on_click=lambda e: print("Link para site de referência 2"),
                    ),
                    ft.IconButton(
                        icon=ft.icons.LINK,
                        icon_color=ft.colors.WHITE,
                        on_click=lambda e: print("Link para site de referência 3"),
                    ),
                    
                ],
            ),
        )

        page.add(
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[navbar, textTitle],
            ),
        )

        videos = []
        with Pyro4.locateNS() as ns:
            for video, videoUri in ns.list(prefix="example.video.").items():
                print("found video", video)
                videos.append(Pyro4.Proxy(videoUri))
        if not videos:
            raise ValueError("no videos found! (have you started the servers first?)")
        
        video_cards = [create_video_card(video, video_data, theme) for video, video_data in zip(videos, video_data_list)]
        
        page.add(
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True,
                spacing=30,
                controls=video_cards,
            )
        )

        page.add(textParagraph, textGroup)

        page.add(
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True,
                spacing=20,
                controls=integrantes_cards,
            )
        )



        page.add(footer)

    create_ui(page)

if __name__ == "__main__":
    ft.app(target=main)
