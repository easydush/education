import { Button, Layout } from 'antd';
import { HeaderCustom } from '../../components/Header';
import React, { FC, useCallback, useEffect, useState } from 'react';
import { getCourse } from "../../api";

import { Course } from '../../types/course';
import { getCurrentCourse } from "../../utils";
import { InfoBlock, PageHeaderText, StyledContent, StyledPageHeader } from "../Main/styles";
import { useParams } from "react-router-dom";
import { subscribe } from "../../api/studying";
import { ModulesList } from "../../components/ModulesList";

export const CourseView = (): JSX.Element => {
  const handleJoin = useCallback(() => {
    subscribe(id);
  }, []);
  const { id } = useParams<{ id: string }>();
  const [loading, setLoading] = useState<boolean>(false);
  const [data, setData] = useState<Course>();
  useEffect(() => {
    async function getData() {
      setLoading(true);
      await setTimeout(() => {
        getCourse(id);
        setData(getCurrentCourse() ?? undefined);
        setLoading(false);
      }, 500);
    }

    getData();
  }, []);
  return (
    <Layout>
      <HeaderCustom />
      <StyledContent>
        <StyledPageHeader title={<PageHeaderText>{data?.title}</PageHeaderText>} backIcon={false} />
        <InfoBlock>
          <h1>{data?.teacher?.name}</h1>
          {data?.teacher?.email}
        </InfoBlock>
        Слушатели: <h3>{data?.listeners}</h3>
        {data?.is_joined}
        {!data?.is_joined ?
          <Button onClick={handleJoin}>Присоединиться</Button> :
          <>
            <h5>Набранный балл: {data?.points}</h5>
            <ModulesList />
          </>
        }
      </StyledContent>
    </Layout>
  );
};
