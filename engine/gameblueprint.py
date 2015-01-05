# engine/gameblueprint.py
# Lillian Lynn Lemmer <lillian.lynn.lemmer@gmail.com>
#
# This module is part of Untitled Game Engine and is released under the
# MIT License: http://opensource.org/licenses/MIT


class GameBlueprint(object):

    def __init__(self, screen, tilemap, viewport, human_player, items=None):
        self.human_player = human_player
        self.tilemap = tilemap
        self.viewport = viewport
        self.items = items or []
        self.screen = screen

    def init(self):
        self.tilemap.convert_layer_images()

    def item_check(self):
        ungot_items = []

        for item in self.items:

            if item.rect.colliderect(self.human_player.rect):
                item.pickup()
            else:
                ungot_items.append(item)

        self.items = ungot_items

    def blit_all(self):
        self.viewport.pan_for_entity(self.human_player)
        self.viewport.blit(self.tilemap.layer_images[0])

        for item in self.items:
            item.blit(self.viewport.surface)

        self.human_player.blit(
                               self.viewport.surface,
                               (
                                self.viewport.start_x,
                                self.viewport.start_y
                               )
                              )

        for layer in self.tilemap.layer_images[1:]:
            self.viewport.blit(layer)

