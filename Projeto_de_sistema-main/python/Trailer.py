# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView

class YoutubeTrailer(QWidget):
    def __init__(self, video_id):
        super().__init__()
        
        # Configurações da janela
        self.setWindowTitle("YouTube Trailer")
        self.setGeometry(100, 100, 800, 600)
        
        # Layout principal
        layout = QVBoxLayout(self)
        self.web_view = QWebEngineView(self)
        layout.addWidget(self.web_view)
        
        # HTML para incorporar o vídeo do YouTube
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {{
                margin: 0;
                overflow: hidden;
                background-color: black;
            }}
        </style>
        </head>
        <body>
            <iframe width="800" height="600" src="https://www.youtube.com/embed/{video_id}"
                    frameborder="0" allowfullscreen></iframe>
        </body>
        </html>
        """
        self.web_view.setHtml(html)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = YoutubeTrailer("oLnS1Ij9-Kk")  # ID de exemplo
    window.show()
    sys.exit(app.exec())