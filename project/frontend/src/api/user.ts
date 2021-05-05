import { UserCredentials } from '../types';
import { apiClient } from './client';
import { AxiosResponse } from 'axios';
import { message } from 'antd';

export const authorize = (userCredentials: UserCredentials): void => {
    apiClient.post('auth/token/login/', userCredentials)
        .then((response: AxiosResponse) => {
            console.log(response);
        })
        .catch(() => {
            message.error('Error with login');
        });
};
