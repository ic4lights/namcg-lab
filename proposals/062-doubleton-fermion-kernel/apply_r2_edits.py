"""062 r2: apply review-r1 replacements R1-R6 verbatim to appH_insert.tex (proposal folder only).
Checks the r1 hash, and that each old string occurs exactly once before and each new string exactly once after."""
import hashlib, os
BS = chr(92)
HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, 'appH_insert.tex')
R1HASH = '8f7c27f5ce2c385e63ee4504d93f9d92bf37dff9aa415edff3851e89915d8902'
b = open(P, 'rb').read()
assert hashlib.sha256(b).hexdigest() == R1HASH, 'r1 hash mismatch'
s = b.decode('ascii')
def L(x): return x.replace('@', BS)  # '@' stands for a backslash in the strings below
R = [
 ('R1', "as irreducible massless representations of fixed helicity~@cite{MackTodorov1969}, as stated in~@cite{Todorov2019}.",
        "as irreducible massless representations of fixed helicity~@cite{MackTodorov1969}, as stated in~@cite{Todorov2019}; for @(n>0@) this uses the identification of the doubleton @(@mathcal H_n@) with a ladder representation, which is taken from the literature on doubletons and not independently verified here."),
 ('R2', "So, for every @(n@), the fermion form of the doubleton member has no normalisable kernel in this class.",
        "So the fermion form of the doubleton member has no normalisable kernel in this class, for @(n=0@) and, given that identification, for every @(n@)."),
 ('R3', "@(@vec J_{@mathrm L}=@tfrac12(@vec J@mp@mathrm i@vec K)@)",
        "@(@vec J_{@mathrm L}=@tfrac12(@vec J@pm@mathrm i@vec K)@)"),
 ('R4', "the Weyl operators @(@mathcal D_+@psi=@sigma^a[@bar T_a,@psi]@) and @(@mathcal D_-@psi=@bar@sigma^a[@bar T_a,@psi]@), with @(@sigma^a=(1,@vec@sigma)@) and @(@bar@sigma^a=(1,-@vec@sigma)@), have trivial kernels.",
        "the Weyl operators @(@mathcal D_@pm@psi=@sigma_@pm^a[@bar T_a,@psi]@) have trivial kernels, where @(@sigma_@pm^a@) are the blocks of @(@Gamma^a@) between the two chiralities of @(@mathfrak{so}(3,1)@), so that @(@sigma_@mp^a@sigma_@pm^b+@sigma_@mp^b@sigma_@pm^a=2@eta^{ab}@)."),
 ('R5', "Nothing here derives the family, @(h_0@), the mass or the fermion content, so Assumption~@ref{ass:lorentzian} is not discharged, and Problem~E remains open and PROGRAMME-CONDITIONAL.",
        "The family, @(h_0@), the mass and the fermion content remain supplied, so this removes one obstruction to the conditional route of the preceding paragraph without deriving the signature, and Problem~E stays open with Assumption~@ref{ass:lorentzian} retained."),
 ('R6', "so @(@mathcal H_0@) restricts to principal series with @(k=0@),",
        "so, by the classification of the unitary dual in~@cite{MartinDussaud2019}, @(@mathcal H_0@) restricts to principal series with @(k=0@),"),
]
for name, old, new in R:
    old, new = L(old), L(new)
    assert s.count(old) == 1, (name, 'old count', s.count(old))
    assert s.count(new) == 0, (name, 'new present before')
    s = s.replace(old, new)
    assert s.count(new) == 1 and s.count(old) == 0, name
    print(name, 'applied: old 1 -> 0, new 0 -> 1')
out = s.encode('ascii')
open(P, 'wb').write(out)
print('r2 insert:', len(out), hashlib.sha256(out).hexdigest())
