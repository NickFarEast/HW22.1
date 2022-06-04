# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def unit_move(self, field, coordinate_x: int, coordinate_y: int, direction: str, is_fly: bool, is_crawl: bool, base_speed = 1):

        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            fly_speed = base_speed * 1.2
            if direction == 'UP':
                new_y = coordinate_y + fly_speed
                new_x = coordinate_x
            elif direction == 'DOWN':
                new_y = coordinate_y - fly_speed
                new_x = coordinate_x
            elif direction == 'LEFT':
                new_y = coordinate_y
                new_x = coordinate_x - fly_speed
            elif direction == 'RIGHT':
                new_y = coordinate_y
                new_x = coordinate_x + fly_speed
        if is_crawl:
            crawl_speed = base_speed * 0.5
            if direction == 'UP':
                new_y = coordinate_y + crawl_speed
                new_x = coordinate_x
            elif direction == 'DOWN':
                new_y = coordinate_y - crawl_speed
                new_x = coordinate_x
            elif direction == 'LEFT':
                new_y = coordinate_y
                new_x = coordinate_x - crawl_speed
            elif direction == 'RIGHT':
                new_y = coordinate_y
                new_x = coordinate_x + crawl_speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
