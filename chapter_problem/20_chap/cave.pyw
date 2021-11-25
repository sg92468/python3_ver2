# cave.pyw - 洞窟探検ゲーム
# 制作にあたってつぎの本の掲載プログラムを全面的に参考にしました
#『ゲームを作りながら楽しく学べるPythonプログラミング』田中賢一郎

import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

# pygame初期化
pygame.init()
pygame.key.set_repeat(5, 5)        # キーを押し続けた時の設定（ms単位）
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()
WALLS = 80                        # 洞窟（穴部分）の分割数
# WALLS個の黒い長方形のリストで表現
# 宇宙船


class 宇宙船():
    # 生成・初期化
    def __init__(self):
        self.x = 0                # 位置（左上隅のx）
        self.y = 250            # 位置（左上隅のy）
        self.vy = 0                # 速度（y方向）
        self.image = pygame.image.load("ship.png")        # 90 x 60
        self.bangimage = pygame.image.load("bang.png")    # 120 x 120

    # 船を表示
    def disp(self):
        SURFACE.blit(self.image, (0, self.y))

    # 爆発の表示
    def bang(self):
        SURFACE.blit(self.bangimage, (0, self.y-40))

# 洞窟


class 洞窟():
    # 生成・初期化
    def __init__(self):
        self.slope = randint(1, 6)
        self.holes = []
        for xpos in range(WALLS):    # リストholesを水平に並んだrectで初期化
            self.holes.append(Rect(xpos * 10, 100, 10, 400))

    # 表示
    def disp(self):
        SURFACE.fill((0, 255, 0))    # 背景（壁）を緑色で塗りつぶす
        for hole in self.holes:        # リストholesの内容だけ黒抜き
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)

    # スクロール
    def scroll(self):
        edge = self.holes[-1].copy()    # 右端のrectをコピー
        test = edge.move(0, self.slope)    # 試しにrectを生成
        if test.top <= 0 or test.bottom >= 600:    # 画面の上下に衝突した場合
            self.slope = randint(1, 6) * (-1 if self.slope > 0 else 1)    # 反転
            edge.inflate_ip(0, -20)        # 上下のサイズを20縮める（難易度UP）
        edge.move_ip(10, self.slope)    # 右に10移動
        self.holes.append(edge)            # リストholesの最後に追加
        del self.holes[0]                # 最初の要素を削除
        self.holes = [x.move(-10, 0) for x in self.holes]    # 順にシフト

    # 衝突判定
    def collision(self, y):
        return self.holes[0].top > y or self.holes[0].bottom < y + 80

# 得点


class 得点():
    # 生成・初期化
    def __init__(self):
        self.point = 0
        self.font = pygame.font.SysFont(None, 36)

    # 得点を画像として表示
    def disp(self, x, y):
        scoreimage = self.font.render(
            "score is {}".format(self.point), True, (0, 0, 225))
        SURFACE.blit(scoreimage, (x, y))

# メイン関数


def main():
    score = 得点()                # 得点を生成
    game_over = False

    ship = 宇宙船()                # 自機を生成
    cave = 洞窟()                # 洞窟を生成

    while True:
        is_space_down = False    # スペースキーは押されていない
        # イベントキューを確認
        for event in pygame.event.get():
            if event.type == KEYDOWN:    # スペースキーが押された
                if event.key == K_SPACE:
                    is_space_down = True
            elif event.type == QUIT:    # 強制終了
                pygame.quit()    # ゲーム終了時の後始末
                sys.exit()

        # 自機を移動
        if not game_over:
            score.point += 10    # 画面更新1回あたり10点獲得
            ship.vy += -3 if is_space_down else 3
            ship.y += ship.vy    # 重力加速度と推力(?)の計算

            # 洞窟をスクロール
            cave.scroll()

            # 衝突判定
            game_over = cave.collision(ship.y)

        # 描画
        cave.disp()                # 洞窟を描く
        ship.disp()                # 宇宙船を描く
        score.disp(600, 20)        # 得点を描く

        if game_over:            # 衝突していたら爆発表示
            ship.bang()            # ループからは出ない

        # ゲーム画面更新
        pygame.display.update()    # 画面を更新
        FPSCLOCK.tick(5)        # 更新速度は5fps


if __name__ == '__main__':
    main()

# 宇宙船と爆発の画像は追加する必要あり。