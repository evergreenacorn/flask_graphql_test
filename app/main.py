from api import app, db
from api import models

from flask import request, jsonify
from api.query import resolve_todos
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML


query = ObjectType("Query")  # инициализируется именем типа, определенного в схеме
# метод связывает todos поле запроса с нашей функцией распознавателя.
query.set_field("todos", resolve_todos)

# Функция принимает имя файла схемы.
# Эта функция проверяет схему и возвращает ее строковое представление.
type_defs = load_schema_from_path("app/schema.graphql")
# Функция берет на себя type_defsпеременная со строковым представлением
# нашей схемы и queryпреобразователь, который мы только что создали.
schema = make_executable_schema(
    type_defs,
    query,
    snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == '__main__':
    app.run(debug=True)
