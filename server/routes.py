from app import app, db
from flask import jsonify, request
from models import Friend


# get all friends
@app.route("/api/friends", methods=["GET"])
def get_all_friends():
    friends = Friend.query.all()
    friends_json = [friend.to_json() for friend in friends]
    return jsonify(friends_json)


#  create a friend
@app.route("/api/friends", methods=["POST"])
def create_friend():
    try:
        data = request.json

        required_fields = ["name", "role", "description", "gender"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return (
                jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}),
                400,
            )

        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")

        if gender == "male":
            img_url = (
                f"https://avatar-placeholder.iran.liara.run/public/boy?username={name}"
            )
        elif gender == "female":
            img_url = (
                f"https://avatar-placeholder.iran.liara.run/public/girl?username={name}"
            )
        else:
            img_url = None

        new_friend = Friend(
            name=name,
            role=role,
            description=description,
            gender=gender,
            img_url=img_url,
        )
        db.session.add(new_friend)
        db.session.commit()
        return jsonify({"msg": "Friend created succesfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"{e}"}), 400


#  delete a friend
@app.route("/api/friends/<int:id>", methods=["DELETE"])
def delete_friend(id):
    try:
        friend = Friend.query.get(id)
        if not friend:
            return jsonify({"error": "Friend not found"}), 404
        db.session.delete(friend)
        db.session.commit()
        return jsonify({"msg": "Friend deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"{e}"}), 400


# update a friend
@app.route("/api/friends/<int:id>", methods=["PATCH"])
def update_friend(id):
    try:
        friend = Friend.query.get(id)
        if not friend:
            return jsonify({"error": "Friend not found"}), 404

        data = request.json
        friend.name = data.get("name", friend.name)
        friend.role = data.get("role", friend.role)
        friend.description = data.get("description", friend.description)
        friend.gender = data.get("gender", friend.gender)

        db.session.commit()
        return jsonify(friend.to_json()), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"{e}"}), 400
