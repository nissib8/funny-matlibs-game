from flask import Flask, render_template, request

app = Flask(__name__)


def school_story(name, color, obj, verb, animal, food, song):

    return f"Today, {name} came to school wearing a {color} hat and carrying a {obj}. During math class, the teacher suddenly started {verb} across the classroom. Everyone screamed when a giant {animal} appeared near the window. At lunch, {name} accidentally spilled {food} on the principal’s shoes and had to sing {song} as punishment."


def vacation_story(place, name, vehicle, food, adjective, verb, plural_animal, obj):

    return f"Last summer, I went to {place} with my best friend {name}. We traveled there using a flying {vehicle} powered entirely by {food}. On the first day, we met a {adjective} tour guide who only communicated by {verb}. At night, a group of {plural_animal} stole our {obj} and disappeared into the jungle."


def horror_story(name, room, obj, animal, food, verb, plural_noun):

    return f"It was midnight when {name} heard a strange noise coming from the {room}. Slowly, they picked up a {obj} and walked toward the sound. Suddenly, a terrifying {animal} jumped out screaming 'Give me your {food}!'. Terrified, {name} escaped by {verb} through the window and landed in a pile of {plural_noun}."


def superhero_story(city, funny_name, superhero_name, superpower, obj, plural_animals, random_phrase, food_item):

    return f"The city of {city} was under attack by the evil villain {funny_name}. Only the superhero {superhero_name} could save the day using their power of {superpower}. Armed with a magical {obj}, they fought thousands of giant {plural_animals} while the crowd chanted '{random_phrase}'. In the end, the villain slipped on a {food_item} and was defeated."


def date_story(name, place, adjective, food, verb, animal, vehicle):

    return f"Yesterday, {name} went on a date to {place} wearing a very {adjective} outfit. Everything was going well until the waiter dropped a plate of {food} onto their lap. Trying to impress their date, they began {verb} on the table while a nearby {animal} stared aggressively. Somehow, the date ended with both of them riding away on a {vehicle} into the sunset."


@app.route("/", methods=["GET", "POST"])
def home():

    story = ""

    if request.method == "POST":

        choice = request.form.get("choice")

        name = request.form.get("name", "")
        color = request.form.get("color", "")
        obj = request.form.get("object", "")
        verb = request.form.get("verb", "")
        animal = request.form.get("animal", "")
        food = request.form.get("food", "")
        song = request.form.get("song", "")
        place = request.form.get("place", "")
        vehicle = request.form.get("vehicle", "")
        adjective = request.form.get("adjective", "")
        plural_animal = request.form.get("plural_animal", "")
        room = request.form.get("room", "")
        plural_noun = request.form.get("plural_noun", "")
        city = request.form.get("city", "")
        funny_name = request.form.get("funny_name", "")
        superhero_name = request.form.get("superhero_name", "")
        superpower = request.form.get("superpower", "")
        plural_animals = request.form.get("plural_animals", "")
        random_phrase = request.form.get("random_phrase", "")
        food_item = request.form.get("food_item", "")

        match choice:

            case "1":
                story = school_story(
                    name, color, obj, verb, animal, food, song
                )

            case "2":
                story = vacation_story(
                    place, name, vehicle, food,
                    adjective, verb, plural_animal, obj
                )

            case "3":
                story = horror_story(
                    name, room, obj, animal,
                    food, verb, plural_noun
                )

            case "4":
                story = superhero_story(
                    city, funny_name, superhero_name,
                    superpower, obj, plural_animals,
                    random_phrase, food_item
                )

            case "5":
                story = date_story(
                    name, place, adjective,
                    food, verb, animal, vehicle
                )

            case _:
                story = "Invalid Choice!"

    return render_template("index.html", story=story)


if __name__ == "__main__":
    app.run(debug=True)