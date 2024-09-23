/* eslint-disable no-undef */
describe("Navigation", () => {
  it("Can navigate to sign up from home", () => {
    cy.visit("/#/");
    cy.get("a").contains("Sign up").click();
    cy.hash().should("eq", "#/sign-up");
  });
});
