export type User = {
    token: string,
};

export const EmptyUser: User = {
    token: '',
};

export type Account = {
    name: string,
    is_student: boolean,
    email: string,
};

export type UserCredentials = {
    email: string,
    password: string,
};

export type RegisterCredentials = {
    name: string,
    is_student: boolean,
    email: string,
    password: string,
    re_password: string,
};

export type ResetCredentials = {
    current_password: string,
    password: string,
    re_password: string,
};

export type ConfirmResetCredentials = {
    uid: string,
    token: string,
    current_password: string,
    password: string,
    re_password: string,
};
