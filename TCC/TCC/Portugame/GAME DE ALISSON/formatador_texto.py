import pygame

group = pygame.sprite.Group


class TextSurface(pygame.sprite.Sprite):
  def __init__(self, image, rect, *groups) -> None:
    super().__init__(*groups)
    self.image = image
    self.rect = rect


def createLine(
  font, text: str, pos: tuple, color=(0, 0, 0), 
  color_bottom=(189, 141, 75), size_limit=340, space_line=20
):
  text = text.split(' ')
  lines = group()

  save_text = ''; save_img = None
  for index, word in enumerate(text):
    new_value = save_text + word if not save_text else save_text + f' {word}'
    img = font.render(new_value, True, color, color_bottom)

    pos_relative = pos[0], pos[1] + (len(lines) * space_line)
    rect = img.get_rect(topleft=pos_relative)

    if rect.width > size_limit:
      if save_img:
        lines.add(TextSurface(save_img, rect))
        save_text = word

        if index == (len(text) - 1):
          img = font.render(word, True, color, color_bottom)
          pos_relative = pos[0], pos[1] + (len(lines) * space_line)
          rect = img.get_rect(topleft=pos_relative)
          lines.add(TextSurface(img, rect))

      else: break
    else: 
      save_text = new_value
      if index == (len(text) - 1):
        lines.add(TextSurface(img, rect))
    
    save_img = img
  
  return lines
