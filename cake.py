import asyncio
import time
import logging

class RussianTeaCake:
    """
    This class is extracted from Classic!
    Russian Tea Cake recipe
    from https://youtu.be/QA0CcTiEMsg

    STEPS:
    1. [2 Minutes] Toast nuts whatever you want.
    2. [2 Minutes] Chop nuts.
    3. [5 Minutes] Mix the butter alone. O
    4. [10 Minutes] Allow the butter to reach room temperature. O
    5. [5 Minutes] Mix the butter, salt, sugar, vanilla. O
    6. [5 Minutes] Mix the butter, salt, sugar, vanilla and nuts with flour. O
    7. [10 Minutes] Roll the dough into balls.
    8. [15 Minutes] Preheat the oven.
    9. [12 Minutes] Bake the cakes.
    10. [3 Minutes] Roll them in powdered sugar.
    """

    def __init__(self, minute: float = 1.0):
        self._minute = minute
        self.__start_time = time.time()
        self.__end_time = None
        self.__chef_is_busy = False;
        self.__toast_nuts = False;
        self.__chop_toasted_nuts = False;
        self.__mix_butter_alone = False;
        self.__allow_ingredients_to_reach_room_temperature = False;
        self.__mix_butter_with_three = False;
        self.__mix_butter_with_three_and_flour_with_nuts = False;
        self.__roll_the_dough_into_balls = False;
        self.__preheat_the_oven = False
        self.__bake_the_cakes = False
        self.__roll_them_in_powdered_sugar = False;

    async def __aenter__(self):
        logging.basicConfig(format='%(levelname)s @ %(asctime)s : %(message)s',
                            datefmt='%d.%m.%Y %H:%M:%S',
                            level=logging.INFO,
                            force=True,
                            handlers=[
                                logging.FileHandler("cake.log", mode='w'),
                                logging.StreamHandler()
                            ])
        logging.getLogger("asyncio").setLevel(logging.WARNING)
        logging.info("[START] Russian Tea Cakes")
        await asyncio.sleep(0)
        return self
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.__end_time = time.time()
        await asyncio.sleep(0)
        logging.info("[END] Russian Tea Cakes")
        if not self.__roll_them_in_powdered_sugar:
            logging.error("The cakes are not baked and !rolled in powdered sugar!")
        logging.info(f"It took {((self.__end_time - self.__start_time)/self._minute):.2f} "
                     f"minutes to complete this recipe.")
        return True


    async def toast_nuts(self) -> None:
        """
        Time: 2 Minutes
        Requires: None ******************************
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy.")
            return None
        self.__chef_is_busy = True
        logging.info("[START] Toasting the nuts")
        await asyncio.sleep(5 * self._minute)
        logging.info("[END] Toasting the nuts")
        self.__chef_is_busy = False
        self.__toast_nuts = True
        return None

    async def chop_toasted_nuts(self) -> None:
        """
        Chop the nuts.
        Time: 2 minutes
        Requires: Toast nuts
        Occupies Chef: Yes
        """
        if not self.__toast_nuts:
            logging.error("The nuts are not toasted")
            return None

        logging.info("[START] Choping nuts")
        await asyncio.sleep(12 * self._minute)
        logging.info("[END] Choping nuts")
        self.__chop_toasted_nuts = True
        return None

    async def mix_butter_alone(self) -> None:
        """
        Mix the butter in a large bowl.
        Time: 5 Minutes
        Requires: Butter at room temperature
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy.")
            return None
        self.__chef_is_busy = True
        logging.info("[START] Mixing the butter alone")
        await asyncio.sleep(5 * self._minute)
        logging.info("[END] Mixing the the butter alone")
        self.__chef_is_busy = False
        self.__mix_butter_alone = True
        return None

    async def allow_ingredients_to_reach_room_temperature(self) -> None:
        """
        Allow the butter to reach room temperature.
        Time: 10 Minutes
        Requires: None ******************************
        Occupies Chef: No
        """
        logging.info("[START] Allowing the ingredients to reach room temperature")
        await asyncio.sleep(10 * self._minute)
        logging.info("[END] Allowing the ingredients to reach room temperature")
        self.__allow_ingredients_to_reach_room_temperature = True
        return None

    async def mix_butter_with_three(self) -> None:
        """
        Mix the butter, salt, sugar, vanilla in a large bowl.
        Time: 5 Minutes
        Requires: Butter at room temperature
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy.")
            return None
        self.__chef_is_busy = True
        logging.info("[START] Mixing the butter with three")
        await asyncio.sleep(5 * self._minute)
        logging.info("[END] Mixing the the butter with three")
        self.__chef_is_busy = False
        self.__mix_butter_with_three = True
        return None

    async def mix_butter_with_three_and_flour_with_nuts(self) -> None:
        """
        Mix the butter, salt, sugar, vanilla in a large bowl.
        Time: 5 Minutes
        Requires: Butter at room temperature
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy.")
            return None
        self.__chef_is_busy = True
        logging.info("[START] Mixing the butter with three, flour and nuts.")
        await asyncio.sleep(5 * self._minute)
        logging.info("[END] Mixing the the butter with three, flour and nuts")
        self.__chef_is_busy = False
        self.__mix_butter_with_three_and_flour_with_nuts = True
        return None

    async def roll_the_dough_into_balls(self) -> None:
        """
        Roll the dough into balls.
        Time: 10 minutes
        Requires: Mixed ingredients
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy")
            return None
        if not self.__mix_butter_with_three_and_flour_with_nuts:
            logging.error("The ingredients are not mixed(all of them)")
            return None
        logging.info("[START] Rolling the dough into balls")
        await asyncio.sleep(10 * self._minute)
        logging.info("[END] Rolling the dough into balls")
        self.__roll_the_dough_into_balls = True
        return None

    async def preheat_the_oven(self) -> None:
        """
        Preheat the oven.
        Time: 15 minutes
        Requires: None
        Occupies Chef: No
        """
        logging.info("[START] Preheating the oven")
        await asyncio.sleep(15 * self._minute)
        logging.info("[END] Preheating the oven")
        self.__preheat_the_oven = True
        return None

    async def bake_the_cakes(self) -> None:
        """
        Bake the cakes.
        Time: 12 minutes
        Requires: Rolled dough into balls and preheated oven
        Occupies Chef: No
        """
        if not self.__roll_the_dough_into_balls:
            logging.error("The dough is not rolled into balls")
            return None
        if not self.__preheat_the_oven:
            logging.error("The oven is not preheated")
            return None
        logging.info("[START] Baking the cakes")
        await asyncio.sleep(12 * self._minute)
        logging.info("[END] Baking the cakes")
        self.__bake_the_cakes = True
        return None

    async def roll_them_in_powdered_sugar(self) -> None:
        """
        Roll them in powdered sugar.
        Time: 1 minute
        Requires: Baked the cakes
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy")
            return None
        if not self.__bake_the_cakes:
            logging.error("The cakes are not baked")
            return None
        logging.info("[START] Rolling them in powdered sugar")
        await asyncio.sleep(1 * self._minute)
        logging.info("[END] Rolling them in powdered sugar")
        self.__roll_them_in_powdered_sugar = True
        return None

async def main() -> None:
    async with RussianTeaCake(0.1) as cake:
        await cake.toast_nuts()
        await cake.chop_toasted_nuts()
        await cake.allow_ingredients_to_reach_room_temperature()
        await cake.mix_butter_alone()
        await cake.mix_butter_with_three()
        await cake.mix_butter_with_three_and_flour_with_nuts()
        await cake.roll_the_dough_into_balls()
        await cake.preheat_the_oven()

        await cake.bake_the_cakes()
        await cake.roll_them_in_powdered_sugar()
    return None

if __name__ == "__main__":
    asyncio.run(main())