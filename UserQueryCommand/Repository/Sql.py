class SqlQueries:
    getUserDetails = """select u.Id as UserId, u.FirstName, u.LastName, u.Email, u.PrimaryContact, u.Country, u.City, u.Gender, u.Age,
                        r.Id as RoleId, r.Role, r.Privilege,
                        p.PaymentType as DefaultPaymentType
                        from users u inner join userroles ur on ur.UserId = u.Id inner join roles r on r.Id = ur.RoleId
                        inner join payments p on p.Id = u.DefaultPaymentMethod where u.Id = {};"""

    submitUserDetails = """update users set
                            FirstName = "{0}",
                            LastName = "{1}",
                            PrimaryContact = "{2}",
                            Country = "{3}",
                            City = "{4}",
                            DefaultPaymentMethod = {5},
                            Age = {6}
                            where Id = {7};"""

    validateUser = """select * from users where UserName = "{0}" and Password = "{1}";"""