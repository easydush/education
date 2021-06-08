import React, { useCallback } from 'react';
import {
    LoginFormWrapper,
    LoginPageWrapper,
    LogoText,
    LogoTextWrapper,
    TabsWrapper,
} from './styles';
import { LoginForm } from '../../components/LoginForm';
import { Tabs } from 'antd';
import { RegisterForm } from '../../components/RegisterForm';
import { authorize } from "../../api";

const { TabPane } = Tabs;
export const Login = (): JSX.Element => {
    return (
        <LoginPageWrapper>
            <LogoTextWrapper>
                <LogoText>
                    EasyLearn
                </LogoText>
            </LogoTextWrapper>
            <LoginFormWrapper>
                <TabsWrapper>
                    <Tabs defaultActiveKey="login">
                        <TabPane tab="Вход" key="login">
                            <LoginForm />
                        </TabPane>
                        <TabPane tab="Регистрация" key="registration">
                            <RegisterForm />
                        </TabPane>
                    </Tabs>
                </TabsWrapper>
            </LoginFormWrapper>
        </LoginPageWrapper>
    );
};
