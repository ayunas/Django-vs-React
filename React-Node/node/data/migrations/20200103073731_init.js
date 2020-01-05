
exports.up = function(knex) {
  return knex.schema.createTable("files", tbl => {
      tbl.increments();
      tbl.string("framework")
        .notNullable();
      tbl.string("folder")
        .notNullable();
      tbl.string("file")
        .notNullable();
  })
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists("files")
};
