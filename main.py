from extensorflowgraphql.application import app, db
from models import sample_model
from ariadne import (load_schema_from_path, make_executable_schema,
                     graphql_sync, snake_case_fallback_resolvers, ObjectType)
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from extensorflowgraphql.queries import resolve_todos, resolve_todo
from extensorflowgraphql.mutations import resolve_create_todo


query = ObjectType("Query")
query.set_field("todo", resolve_todo)
query.set_field("todos", resolve_todos)
mutation = ObjectType("Mutation")
mutation.set_field("createTodo", resolve_create_todo)
type_defs = load_schema_from_path("schemas/schema.graphql")
type_defs_scm = load_schema_from_path("schemas/schema_scm.graphql")
schema = make_executable_schema([type_defs, type_defs_scm], query)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)
    status_code = 200 if success else 400

    return jsonify(result), status_code


